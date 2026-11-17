# Public Bus Live Tracking & Crowding Estimator — Individual Project Submission

| | |
|---|---|
| **Student** | Meghna |
| **SRN** | PES1UG24CS269 |
| **BPS** | #24 |
| **Problem statement** | #24 — Smart Cities, Transport & Logistics: *Public Bus Live Tracking & Crowding Estimator* |
| **Actors** | Commuter, Fleet Controller |
| **GitHub repository** | _add link here_ |

**The system in one paragraph:** a municipal transit intelligence platform that ingests GPS feeds from city buses, estimates arrival times (ETA) at downstream stops, and computes passenger crowding levels from ticketing sensors. Commuters see live bus status; Fleet Controllers monitor the fleet and receive delay and crowding alerts.

## Repository structure

| # | Folder | Contents | Status |
|---|---|---|---|
| 1 | [`1-RE/`](1-RE/) | Requirements Engineering: FR and NFR table, RTM, use-case diagram, UC-01 flow specification | Done |
| 2 | [`2-Project-Creation-Screenshots/`](2-Project-Creation-Screenshots/) | Jira Kanban, Scrum and Bug Tracker screenshots and reports; GitHub repo creation screenshot | Jira done; GitHub screenshots to add | Jira done; GitHub screenshots to add |
| 3 | [`3-Architecture/`](3-Architecture/) | Lab 3: UML component diagram and one-page architecture justification (PDF) | Done |
| 4 | [`4-SRS-and-WBS/`](4-SRS-and-WBS/) | Software Requirements Specification and Work Breakdown Structure | Done |
| 5 | [`5-Copilot-Code/`](5-Copilot-Code/) | GitHub Copilot generated code: screenshots or repository link | Done |

## 1. Requirements Engineering — [`1-RE/`](1-RE/)
| File | Description |
|---|---|
| [`Requirements_Table.xlsx`](1-RE/Requirements_Table.xlsx) | 5 functional (FR-001 to FR-005) and 2 non-functional (NFR-001, NFR-002) requirements, each with ID, type, description, priority, acceptance criteria and rationale |
| [`RTM.xlsx`](1-RE/RTM.xlsx) | Requirements Traceability Matrix: requirement → use case → design component → Jira item → test case → bug |
| [`UseCase_Diagram.pdf`](1-RE/UseCase_Diagram.pdf) | UML use-case diagram (6 use cases, includes `«include»` and `«extend»`) |
| [`UC-01_View_Live_Bus_Status_Flow_Spec.pdf`](1-RE/UC-01_View_Live_Bus_Status_Flow_Spec.pdf) | Flow specification: preconditions, postconditions, main success scenario, alternate flow |

## 2. Project creation screenshots — [`2-Project-Creation-Screenshots/`](2-Project-Creation-Screenshots/README.md)
Jira spaces `Kanban_BPS#24`, `Scrum_BPS#24` and `BugTracker_BPS#24`, with an index of every screenshot and its report PDF. GitHub creation screenshots go in `github/`.

## 3. Architecture (Lab 3) — [`3-Architecture/`](3-Architecture/README.md)
- [`Bus_Tracking_Component_Diagram.pdf`](3-Architecture/Bus_Tracking_Component_Diagram.pdf) — UML component diagram: 14 components and their provided/required interfaces, in a layered architecture with an event queue between the ingestion and processing layers.
- [`Architecture_Justification.pdf`](3-Architecture/Architecture_Justification.pdf) — one-page justification: *We chose Layered Architecture for the Public Bus Live Tracking & Crowding Estimator System.*

## 4. SRS and WBS — [`4-SRS-and-WBS/`](4-SRS-and-WBS/)
- [`SRS.md`](4-SRS-and-WBS/SRS.md) — Software Requirements Specification
- [`WBS.md`](4-SRS-and-WBS/WBS.md) — Work Breakdown Structure mapped to Jira epics, stories, tasks and sprint

## 5. GitHub Copilot generated code — [`5-Copilot-Code/`](5-Copilot-Code/README.md)
A Python console app (standard library only) that simulates five buses on a six-stop route: GPS and ticketing ingestion, ETA, crowding, and delay/crowding alerts, with Commuter and Fleet Controller views and unit tests. Run instructions are in the folder README.

