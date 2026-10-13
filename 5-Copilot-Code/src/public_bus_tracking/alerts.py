"""Fleet alert generation."""

from .crowding import estimate_crowding
from .models import Bus


def alerts_for_bus(bus: Bus) -> list[str]:
    """Return human-readable alerts for delay and crowding conditions."""
    alerts: list[str] = []
    if bus.delay_minutes > 5:
        alerts.append(
            f"{bus.bus_id}: delay is {bus.delay_minutes:.1f} minutes (over 5 minutes)"
        )
    if estimate_crowding(bus.passenger_count, bus.capacity) == "High":
        alerts.append(f"{bus.bus_id}: crowding level is High")
    return alerts


def generate_alerts(buses: list[Bus]) -> list[str]:
    """Generate alerts for all buses in the fleet."""
    return [alert for bus in buses for alert in alerts_for_bus(bus)]
