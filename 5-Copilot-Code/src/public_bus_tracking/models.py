"""Shared data models for the simulated bus network."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Stop:
    name: str
    distance_km: float


@dataclass(frozen=True)
class Route:
    name: str
    stops: tuple[Stop, ...]
    length_km: float
    start_latitude: float = 37.7749
    start_longitude: float = -122.4194

    def coordinates_at(self, distance_km: float) -> tuple[float, float]:
        """Return a simulated GPS coordinate along a straight route."""
        fraction = min(max(distance_km / self.length_km, 0.0), 1.0)
        return (
            self.start_latitude + fraction * 0.05,
            self.start_longitude + fraction * 0.05,
        )


@dataclass
class Bus:
    bus_id: str
    route_name: str
    position_km: float
    speed_kmh: float
    passenger_count: int
    capacity: int
    delay_minutes: float
    latitude: float
    longitude: float
    last_gps_update: datetime
    last_eta_seconds: dict[str, float] = field(default_factory=dict)
