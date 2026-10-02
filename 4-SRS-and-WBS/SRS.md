# Software Requirements Specification (SRS)

**Project:** Public Bus Live Tracking & Crowding Estimator (Problem Statement #24 — Smart Cities, Transport & Logistics)  
**Student:** Meghna | PES1UG24CS269 | BPS#24  
**Version:** 1.0 | **Status:** Draft for submission

---

## 1. Introduction

### 1.1 Purpose
This document specifies the requirements for a municipal transit intelligence platform that ingests GPS feeds from city buses, estimates arrival times (ETA) at downstream stops, and computes passenger crowding levels from ticketing sensors. It is intended for the course evaluators, and for any developer or tester building or verifying the system.

### 1.2 Scope
The system provides:
- Live bus location and ETA information to **Commuters**.
- Fleet-wide operational monitoring and proactive delay/crowding alerts to **Fleet Controllers**.

Out of scope: ticket sales or payment, route planning/scheduling tools, driver-facing applications, and hardware design of GPS units and ticketing sensors.

### 1.3 Definitions and abbreviations
| Term | Meaning |
|---|---|
| ETA | Estimated time of arrival of a bus at a stop |
| GPS telemetry | Location data periodically sent by a bus |
| Crowding level | Passenger load of a bus, classified as Low / Medium / High |
| Delay | Minutes a bus is behind its schedule |
| FR / NFR | Functional / Non-Functional Requirement |
| UC | Use case |
| RTM | Requirements Traceability Matrix |

### 1.4 References
- Problem statement: [`../1-RE/Problem_Statement_24.pdf`](../1-RE/Problem_Statement_24.pdf)
- Requirements table: [`../1-RE/Requirements_Table.xlsx`](../1-RE/Requirements_Table.xlsx) and [`../1-RE/Requirements.md`](../1-RE/Requirements.md)
- Use-case diagram and UC-01 flow specification: [`../1-RE/`](../1-RE/)
- RTM: [`../1-RE/RTM.md`](../1-RE/RTM.md)
- Architecture: [`../2-Architecture/`](../2-Architecture/README.md)
- Work breakdown: [`WBS.md`](WBS.md)

---

## 2. Overall description

### 2.1 Product perspective
A standalone platform fed by two external sources (the Bus GPS Feed and the Ticketing Sensor/System) and used through a Commuter-facing app (web/mobile) and a Fleet Controller dashboard. See the architecture diagram in `2-Architecture/`.

### 2.2 Users (actors)
| Actor | Type | Description |
|---|---|---|
| Commuter | Primary | Member of the public who wants to know where a bus is, when it will arrive and how crowded it is |
| Fleet Controller | Primary | Transit operator staff who monitor the active fleet and respond to delays and overcrowding |
| Bus GPS Feed | External system | Supplies bus GPS coordinates |
| Ticketing Sensor/System | External system | Supplies ticketing/occupancy data used for crowding estimates |

### 2.3 Product functions (summary)
1. Ingest bus GPS data and recalculate ETAs (UC-02, UC-03).
2. Let Commuters view live bus status (UC-01).
3. Estimate passenger crowding (UC-04).
4. Let Fleet Controllers monitor the fleet (UC-05).
5. Alert Fleet Controllers to delays and high crowding (UC-06).

### 2.4 Operating environment
Server-side platform processing continuous telemetry; clients are a web or mobile application for Commuters and a web dashboard for Fleet Controllers.

### 2.5 Assumptions and dependencies
- Buses report GPS position every 5 seconds (FR-001); ticketing sensors report occupancy data regularly.
- Route and schedule data (stops, timetables) exists in the system and is kept up to date.
- Commuters and Fleet Controllers have network access to the platform.
- Technology choices (languages, databases, cloud provider) are not fixed by this SRS.

---

## 3. System features and use cases

| ID | Use case | Primary actor | Relationships |
|---|---|---|---|
| UC-01 | View Live Bus Status | Commuter | «include» UC-03 and UC-04 |
| UC-02 | Ingest GPS Telemetry | Bus GPS Feed | Supports UC-03 |
| UC-03 | Calculate Bus ETA | Bus GPS Feed | «include» relationship with UC-02 |
| UC-04 | Estimate Passenger Crowding | Ticketing Sensor/System | Included by UC-01 |
| UC-05 | Monitor Fleet | Fleet Controller | Extended by UC-06 |
| UC-06 | Receive Delay/Crowding Alert | Fleet Controller | «extend» UC-05 (when a threshold is crossed) |

The diagram is in [`../1-RE/UseCase_Diagram.pdf`](../1-RE/UseCase_Diagram.pdf). The full flow for **UC-01** (preconditions, postconditions, main success scenario and alternate flow 3a for stale GPS data) is in [`../1-RE/UC-01_View_Live_Bus_Status_Flow_Spec.pdf`](../1-RE/UC-01_View_Live_Bus_Status_Flow_Spec.pdf).

**UC-01 summary.** The Commuter selects a route, stop or bus; the system obtains the current ETA (UC-03) and crowding level (UC-04) for each relevant bus, assembles the live-status view and displays it. If no GPS update has been received for a bus within 15 seconds (three missed 5-second cycles), the bus is shown as "Live data unavailable" instead of a stale ETA.

---

## 4. Specific requirements

### 4.1 Functional requirements
| ID | Priority | Requirement | Acceptance criteria |
|---|---|---|---|
| FR-001 | High | The system shall ingest bus GPS coordinates every 5 seconds and recalculate arrival ETAs for all upcoming route stops. | Pass: ETA updates based on current traffic speed and distance.<br>Fail: ETA increases while bus approaches stop. |
| FR-002 | High | The system shall allow a Commuter to view the live status (current location, ETA, and crowding level) of buses for a route or stop that the Commuter selects. | Pass: Selecting a valid route/stop displays current location, ETA, and crowding level for all buses serving it within 3 seconds.<br>Fail: No status is displayed, or the displayed data is more than one telemetry cycle (5s) old with no staleness indicator. |
| FR-003 | High | The system shall estimate a passenger crowding level (Low/Medium/High) for each active bus using ticketing sensor data. | Pass: A crowding level is computed and refreshed within 30 seconds of new ticketing sensor data being received for a bus.<br>Fail: Crowding level is missing, or is not refreshed within 30 seconds of new sensor data. |
| FR-004 | High | The system shall allow a Fleet Controller to monitor the operational status of all active buses, including current delay (minutes behind schedule) and crowding level. | Pass: The fleet dashboard lists every currently active bus together with its delay in minutes and crowding level, refreshed within 10 seconds of the latest telemetry.<br>Fail: Any active bus is missing from the dashboard, or its delay/crowding data is older than 10 seconds without a stale-data indicator. |
| FR-005 | Medium | The system shall generate an operational alert to the Fleet Controller when a bus's delay exceeds 5 minutes or its crowding level reaches High. | Pass: An alert referencing the bus and the triggering condition (delay or crowding) is created and delivered to the Fleet Controller within 15 seconds of the threshold being crossed.<br>Fail: No alert is generated within 15 seconds of a qualifying condition, or the alert omits the bus identifier or triggering condition. |

### 4.2 Non-functional requirements
| ID | Priority | Requirement | Acceptance criteria |
|---|---|---|---|
| NFR-001 | High | The tracking engine shall handle telemetry streams from up to 1,000 active transit vehicles simultaneously. | Pass: Benchmarking tests confirm target latency and security standards under simulated peak load. |
| NFR-002 | High | The system shall propagate an updated bus location and ETA to the Commuter-facing display within 10 seconds of receiving the corresponding GPS telemetry update, for at least 99% of updates. | Pass: End-to-end monitoring logs show propagation latency (telemetry receipt to display update) of 10 seconds or less for at least 99% of sampled updates over a peak-hour test window.<br>Fail: More than 1% of sampled updates exceed 10 seconds, or logs are unavailable to verify the threshold. |

Rationale for each requirement is recorded in [`../1-RE/Requirements.md`](../1-RE/Requirements.md).

### 4.3 External interface requirements
| Interface | Description |
|---|---|
| Bus GPS Feed → system | Periodic GPS coordinates per bus (every 5 s) |
| Ticketing Sensor/System → system | Passenger/ticketing data used for the crowding estimate |
| Commuter application | Web/mobile UI showing location, ETA and crowding level per bus |
| Fleet Controller dashboard | Web UI listing all active buses with delay and crowding, plus alerts |

### 4.4 Design constraints and quality attributes
- **Performance:** support 1,000 simultaneous vehicles (NFR-001); propagate updates within 10 s for at least 99% of updates (NFR-002).
- **Security:** telemetry data must be protected in transit and access to the dashboard restricted to authorised Fleet Controllers (NFR-001).
- **Data freshness:** stale data must be flagged rather than shown as current (FR-002, FR-004, UC-01 alternate flow).

---

## 5. Traceability
Every requirement is traced to use cases, design components, Jira work items, planned test cases and bugs in [`../1-RE/RTM.md`](../1-RE/RTM.md).

## 6. Known open items
- Test cases listed in the RTM are planned; execution results are to be added.
- Three defects are logged in Jira (BUG24-1, BUG24-2, BUG24-3) and relate to FR-001/FR-002, FR-003 and FR-005.
