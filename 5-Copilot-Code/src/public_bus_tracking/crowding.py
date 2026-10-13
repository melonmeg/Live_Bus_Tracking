"""Passenger-count based crowding estimates."""


def estimate_crowding(passenger_count: int, capacity: int) -> str:
    """Classify occupancy as Low, Medium, or High."""
    if capacity <= 0:
        raise ValueError("Bus capacity must be greater than zero.")
    if passenger_count < 0:
        raise ValueError("Passenger count cannot be negative.")

    occupancy = passenger_count / capacity
    if occupancy < 0.5:
        return "Low"
    if occupancy < 0.8:
        return "Medium"
    return "High"
