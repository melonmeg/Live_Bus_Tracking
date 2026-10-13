# Public Bus Live Tracking & Crowding Estimator

A small Python console app that simulates five buses on a six-stop route. It
uses generated GPS positions and ticketing-sensor passenger counts; no external
APIs or third-party Python packages are required.

## Run

From the project root, use Python 3.10 or newer:

```powershell
python src\main.py
```

Choose a commuter route view, a stop-specific view, or the Fleet Controller
view. Simulated GPS and ticketing readings refresh every five seconds while
the menu is running. The route view includes each bus's simulated coordinates,
ETAs to upcoming stops, and crowding level. Fleet monitoring shows delay and
crowding, with alerts for delays over five minutes and High crowding. When a
bus has not sent GPS telemetry for more than 15 seconds, its ETA is reported as
`Live data unavailable`.

The route is a local straight-line simulation with stops at Central Station,
Market Street, Civic Center, University, Riverside Park, and Harbor Terminal.
ETA estimates for a stop are capped at their previous value so they never
increase while the bus approaches it.

## Tests

Run the unit tests from the project root:

```powershell
python -m unittest discover -s tests -v
```
