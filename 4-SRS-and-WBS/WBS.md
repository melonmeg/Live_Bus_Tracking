# Work Breakdown Structure (WBS)

**Project:** Public Bus Live Tracking & Crowding Estimator (PS #24) | **Student:** Meghna | PES1UG24CS269 | BPS#24

The WBS follows the Jira hierarchy (Epic → Requirement/Story → Task) created in the Kanban and Scrum spaces (see `../3-Project-Creation-Screenshots/`), and groups the work into project phases.

## 1. Phase view

| WBS | Work package | Output |
|---|---|---|
| 1.0 | Requirements Engineering | Requirements table (5 FR, 2 NFR), use-case diagram, UC-01 flow spec, RTM → `1-RE/` |
| 2.0 | Architecture & Design | Architecture diagram → `2-Architecture/` |
| 3.0 | Project set-up & tracking | GitHub repo; Jira Kanban, Scrum and Bug Tracker spaces → `3-Project-Creation-Screenshots/` |
| 4.0 | Specification | SRS and WBS → `4-SRS-and-WBS/` |
| 5.0 | Implementation (with GitHub Copilot) | Source code → `5-Copilot-Code/` *(pending)* |
| 6.0 | Testing & defect fixing | Test execution, bug fix, retest → `6-Testing-Tools/` *(pending)* |

## 2. Implementation breakdown (Jira epics, stories, tasks)

### Epic A — Live Bus Tracking and Passenger Information (KBPS24-22 / SBPS24-24)
| WBS | Requirement / story | Jira (Kanban / Scrum) | Task |
|---|---|---|---|
| 5.1 | FR-001 — Ingest GPS Telemetry and Recalculate ETA | KBPS24-1 / SBPS24-2 | |
| 5.1.1 | Story: Process Live GPS Telemetry and Recalculate ETA | KBPS24-14 / SBPS24-10 | KBPS24-23 Implement GPS Telemetry Processing |
| 5.2 | FR-002 — View Live Bus Status | KBPS24-2 / SBPS24-3 | |
| 5.2.1 | Story: View Live Bus Status | KBPS24-15 / SBPS24-11 | KBPS24-24 Develop Live Bus Status Interface |
| 5.3 | Story: Estimate Passenger Crowding | KBPS24-16 / SBPS24-12 | KBPS24-25 Implement Crowding Estimation Module |

### Epic B — Passenger Crowding and Fleet Monitoring (KBPS24-30 / SBPS24-25)
| WBS | Requirement / story | Jira (Kanban / Scrum) | Task |
|---|---|---|---|
| 5.4 | FR-003 — Estimate Passenger Crowding | KBPS24-3 / SBPS24-4 | (implemented via story KBPS24-16 above) |
| 5.5 | FR-004 — Monitor Fleet Operational Status | KBPS24-4 / SBPS24-5 | |
| 5.5.1 | Story: Monitor Fleet Operational Status | KBPS24-17 / SBPS24-13 | KBPS24-26 Develop Fleet Monitoring Dashboard |
| 5.6 | Story: Generate Delay and Crowding Alerts | KBPS24-18 / SBPS24-14 | KBPS24-27 Implement Alert Generation Service |

### Epic C — Operational Alerts and System Scalability (KBPS24-31 / SBPS24-26)
| WBS | Requirement / story | Jira (Kanban / Scrum) | Task |
|---|---|---|---|
| 5.7 | FR-005 — Generate Delay and Crowding Alerts | KBPS24-5 / SBPS24-6 | (implemented via story KBPS24-18 above) |
| 5.8 | NFR-001 — Support 1000 Concurrent Transit Vehicles | KBPS24-6 / SBPS24-7 | |
| 5.8.1 | Story: Support 1000 Concurrent Transit Vehicles | KBPS24-19 / SBPS24-15 | KBPS24-28 Implement Scalability and Load Handling |
| 5.9 | NFR-002 — Propagate Live Updates Within 10 Seconds | KBPS24-7 / SBPS24-8 | |
| 5.9.1 | Story: Maintain Live Update Latency Within 10 Seconds | KBPS24-20 / SBPS24-16 | KBPS24-29 Optimize Real-Time Update Pipeline |

## 3. Sprint planning (Scrum)

Sprint **SBPS24 Sprint 2** (3–10 Sep 2026) carried **16 story points** (see `scrum-05-sprint-board.png` and `scrum-06-sprint-burndown.png`):

| Story | Points | State on the sprint board |
|---|---|---|
| SBPS24-14 Generate Delay and Crowding Alerts | 3 | Done |
| SBPS24-13 Monitor Fleet Operational Status | 5 | In Progress |
| SBPS24-15 Support 1000 Concurrent Transit Vehicles | 8 | To Do |

## 4. Defect tracking (Bug Tracker space)

| Bug | Title | Related requirement |
|---|---|---|
| BUG24-1 | Live Bus Location and ETA Are Not Updated Correctly | FR-001, FR-002, NFR-002 |
| BUG24-2 | Incorrect Passenger Crowding Level Is Displayed | FR-003 |
| BUG24-3 | Delay Alert Is Not Generated When Delay Exceeds Five Minutes | FR-005 |
