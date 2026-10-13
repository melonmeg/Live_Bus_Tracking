"""Deterministic local GPS and ticketing-sensor simulation."""

import random
from datetime import datetime

from .models import Bus, Route, Stop

GPS_INTERVAL_SECONDS = 5
BUS_CAPACITY = 50


def make_default_route() -> Route:
    """Build the six-stop route used by the console app."""
    stops = tuple(
        Stop(name, distance)
        for name, distance in (
            ("Central Station", 0.0),
            ("Market Street", 2.0),
            ("Civic Center", 4.0),
            ("University", 6.0),
            ("Riverside Park", 8.0),
            ("Harbor Terminal", 10.0),
        )
    )
    return Route(name="Route 1", stops=stops, length_km=10.0)


class FleetSimulator:
    """Simulates GPS telemetry and ticketing counts for five buses."""

    def __init__(
        self, route: Route, now: datetime | None = None, seed: int = 7
    ) -> None:
        self.route = route
        self.random = random.Random(seed)
        timestamp = now or datetime.now()
        self.buses: list[Bus] = []

        for index in range(5):
            position = 0.4 + index * 1.4
            latitude, longitude = route.coordinates_at(position)
            self.buses.append(
                Bus(
                    bus_id=f"BUS-{index + 1:03}",
                    route_name=route.name,
                    position_km=position,
                    speed_kmh=24 + index * 2,
                    passenger_count=self.random.randint(8, BUS_CAPACITY),
                    capacity=BUS_CAPACITY,
                    delay_minutes=float(index * 2),
                    latitude=latitude,
                    longitude=longitude,
                    last_gps_update=timestamp,
                )
            )

    def send_gps_updates(
        self, elapsed_seconds: int = GPS_INTERVAL_SECONDS, now: datetime | None = None
    ) -> None:
        """Advance each bus, refresh its GPS timestamp, and sample ticket counts."""
        timestamp = now or datetime.now()
        for bus in self.buses:
            distance = bus.speed_kmh * elapsed_seconds / 3600
            next_position = bus.position_km + distance
            if next_position >= self.route.length_km:
                next_position %= self.route.length_km
                bus.last_eta_seconds.clear()

            bus.position_km = next_position
            bus.latitude, bus.longitude = self.route.coordinates_at(next_position)
            bus.passenger_count = min(
                bus.capacity,
                max(0, bus.passenger_count + self.random.randint(-2, 3)),
            )
            bus.last_gps_update = timestamp
