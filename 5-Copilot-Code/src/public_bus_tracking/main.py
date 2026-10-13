"""Interactive console interface for commuters and fleet controllers."""

import threading
from datetime import datetime

from .alerts import generate_alerts
from .crowding import estimate_crowding
from .eta import calculate_upcoming_etas, format_eta
from .ingestion import GPS_INTERVAL_SECONDS, FleetSimulator, make_default_route
from .models import Bus


def show_bus_status(simulator: FleetSimulator, stop_name: str | None = None) -> None:
    """Display each bus's current simulated location, ETA, and crowding."""
    now = datetime.now()
    route = simulator.route
    print(f"\n{route.name}" + (f" — {stop_name}" if stop_name else ""))
    for bus in simulator.buses:
        crowding = estimate_crowding(bus.passenger_count, bus.capacity)
        etas = calculate_upcoming_etas(bus, route, now)
        if (now - bus.last_gps_update).total_seconds() >= 15:
            eta_text = "Live data unavailable"
        elif stop_name:
            eta_text = (
                format_eta(etas[stop_name])
                if stop_name in etas
                else "Stop passed / no ETA"
            )
        else:
            eta_text = ", ".join(
                f"{name}: {format_eta(seconds)}" for name, seconds in etas.items()
            ) or "No upcoming stops"

        print(
            f"{bus.bus_id} | {bus.latitude:.5f}, {bus.longitude:.5f} | "
            f"ETA: {eta_text} | Crowding: {crowding}"
        )


def show_fleet(simulator: FleetSimulator) -> None:
    """Display active fleet delay and crowding information."""
    print("\nActive fleet")
    for bus in simulator.buses:
        live_label = (
            "Live"
            if (datetime.now() - bus.last_gps_update).total_seconds() < 15
            else "Live data unavailable"
        )
        print(
            f"{bus.bus_id} | {live_label} | Delay: {bus.delay_minutes:.1f} min | "
            f"Crowding: {estimate_crowding(bus.passenger_count, bus.capacity)}"
        )

    alerts = generate_alerts(simulator.buses)
    print("\nAlerts")
    for alert in alerts:
        print(f"- {alert}")
    if not alerts:
        print("No active alerts.")


def _telemetry_worker(
    simulator: FleetSimulator, stop_event: threading.Event, lock: threading.Lock
) -> None:
    """Refresh simulated sensor data on the requested five-second cadence."""
    while not stop_event.wait(GPS_INTERVAL_SECONDS):
        with lock:
            simulator.send_gps_updates()


def run_console() -> None:
    route = make_default_route()
    simulator = FleetSimulator(route)
    lock = threading.Lock()
    stop_event = threading.Event()
    worker = threading.Thread(
        target=_telemetry_worker,
        args=(simulator, stop_event, lock),
        daemon=True,
    )
    worker.start()

    print("Public Bus Live Tracking & Crowding Estimator")
    print(
        f"Simulating five buses on {route.name} with GPS and ticketing updates "
        f"every {GPS_INTERVAL_SECONDS} seconds."
    )
    try:
        while True:
            print("\n1. Commuter: choose a route")
            print("2. Commuter: view a stop")
            print("3. Fleet Controller: monitor buses and alerts")
            print("4. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                print("1. Route 1")
                route_selection = input("Choose a route: ").strip()
                if route_selection == "1":
                    with lock:
                        show_bus_status(simulator)
                else:
                    print("Invalid route selection.")
            elif choice == "2":
                for index, stop in enumerate(route.stops, start=1):
                    print(f"{index}. {stop.name}")
                selection = input("Choose a stop: ").strip()
                if selection.isdigit() and 1 <= int(selection) <= len(route.stops):
                    with lock:
                        show_bus_status(simulator, route.stops[int(selection) - 1].name)
                else:
                    print("Invalid stop selection.")
            elif choice == "3":
                with lock:
                    show_fleet(simulator)
            elif choice == "4":
                break
            else:
                print("Invalid option. Choose 1, 2, 3, or 4.")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
    finally:
        stop_event.set()
        worker.join(timeout=GPS_INTERVAL_SECONDS + 1)


if __name__ == "__main__":
    run_console()
