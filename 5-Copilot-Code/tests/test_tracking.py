"""Unit tests for ETA, crowding, and fleet alerts."""

import sys
import unittest
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from public_bus_tracking.alerts import alerts_for_bus  # noqa: E402
from public_bus_tracking.crowding import estimate_crowding  # noqa: E402
from public_bus_tracking.eta import calculate_upcoming_etas  # noqa: E402
from public_bus_tracking.ingestion import FleetSimulator, make_default_route  # noqa: E402


class TrackingTests(unittest.TestCase):
    def test_eta_to_each_upcoming_stop_decreases_or_stays_constant(self) -> None:
        route = make_default_route()
        now = datetime(2026, 1, 1, 12, 0, 0)
        simulator = FleetSimulator(route, now=now)
        bus = simulator.buses[0]

        first_estimates = calculate_upcoming_etas(bus, route, now)
        bus.position_km += 0.1
        bus.speed_kmh = 10
        bus.last_gps_update = now + timedelta(seconds=5)
        later_estimates = calculate_upcoming_etas(
            bus, route, now + timedelta(seconds=5)
        )

        for stop_name, eta in later_estimates.items():
            self.assertLessEqual(eta, first_estimates[stop_name])

    def test_eta_omits_stops_behind_bus(self) -> None:
        route = make_default_route()
        now = datetime(2026, 1, 1, 12, 0, 0)
        simulator = FleetSimulator(route, now=now)
        bus = simulator.buses[0]
        bus.position_km = 4.0

        estimates = calculate_upcoming_etas(bus, route, now)

        self.assertNotIn("Civic Center", estimates)
        self.assertIn("University", estimates)

    def test_crowding_thresholds(self) -> None:
        self.assertEqual(estimate_crowding(24, 50), "Low")
        self.assertEqual(estimate_crowding(25, 50), "Medium")
        self.assertEqual(estimate_crowding(40, 50), "High")

    def test_alerts_trigger_for_delay_and_high_crowding(self) -> None:
        route = make_default_route()
        bus = FleetSimulator(route).buses[0]
        bus.delay_minutes = 5.1
        bus.passenger_count = 40

        alerts = alerts_for_bus(bus)

        self.assertEqual(len(alerts), 2)
        self.assertTrue(any("BUS-001" in alert and "delay" in alert for alert in alerts))
        self.assertTrue(
            any("BUS-001" in alert and "crowding" in alert for alert in alerts)
        )

    def test_eta_is_unavailable_for_stale_gps(self) -> None:
        route = make_default_route()
        now = datetime(2026, 1, 1, 12, 0, 15)
        simulator = FleetSimulator(route, now=now - timedelta(seconds=15))

        self.assertEqual(calculate_upcoming_etas(simulator.buses[0], route, now), {})


if __name__ == "__main__":
    unittest.main()
