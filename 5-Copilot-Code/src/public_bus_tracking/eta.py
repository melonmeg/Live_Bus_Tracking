"""ETA calculations for upcoming stops."""

from datetime import datetime

from .models import Bus, Route


def calculate_upcoming_etas(
    bus: Bus, route: Route, now: datetime | None = None
) -> dict[str, float]:
    """Return ETA seconds for upcoming stops, never increasing per stop."""
    current_time = now or datetime.now()
    if (current_time - bus.last_gps_update).total_seconds() >= 15:
        return {}
    if bus.speed_kmh <= 0:
        return {}

    estimates: dict[str, float] = {}
    for stop in route.stops:
        if stop.distance_km <= bus.position_km:
            continue

        seconds = (stop.distance_km - bus.position_km) / bus.speed_kmh * 3600
        # A changed speed can make a raw estimate rise; retain the best estimate
        # already shown until the bus reaches that stop.
        seconds = min(seconds, bus.last_eta_seconds.get(stop.name, seconds))
        estimates[stop.name] = seconds

    bus.last_eta_seconds.update(estimates)
    return estimates


def format_eta(seconds: float) -> str:
    """Format an ETA as whole minutes."""
    minutes = max(0, round(seconds / 60))
    return f"{minutes} min"
