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
| 2 | [`2-Architecture/`](2-Architecture/) | Architecture diagram and component description | Done |
| 3 | [`3-Project-Creation-Screenshots/`](3-Project-Creation-Screenshots/) | Jira Kanban, Scrum and Bug Tracker screenshots and reports; GitHub repo creation screenshots | Jira done; GitHub screenshots to add |
| 4 | [`4-SRS-and-WBS/`](4-SRS-and-WBS/) | Software Requirements Specification and Work Breakdown Structure | Done |
| 5 | [`5-Copilot-Code/`](5-Copilot-Code/) | GitHub Copilot generated code: screenshots or repository link | Pending |
| 6 | [`6-Testing-Tools/`](6-Testing-Tools/) | Software testing practice: run tests, fix the bug with vibe coding, retest, repository link | Pending |

## 1. Requirements Engineering — [`1-RE/`](1-RE/)
| File | Description |
|---|---|
| [`Requirements.md`](1-RE/Requirements.md) / [`Requirements_Table.xlsx`](1-RE/Requirements_Table.xlsx) | 5 functional (FR-001 to FR-005) and 2 non-functional (NFR-001, NFR-002) requirements, each with ID, type, description, priority, acceptance criteria and rationale |
| [`RTM.md`](1-RE/RTM.md) / [`RTM.xlsx`](1-RE/RTM.xlsx) | Requirements Traceability Matrix: requirement → use case → design component → Jira item → test case → bug |
| [`UseCase_Diagram.pdf`](1-RE/UseCase_Diagram.pdf) / [`.png`](1-RE/UseCase_Diagram.png) | UML use-case diagram (6 use cases, includes `«include»` and `«extend»`) |
| [`UC-01_View_Live_Bus_Status_Flow_Spec.pdf`](1-RE/UC-01_View_Live_Bus_Status_Flow_Spec.pdf) | Flow specification: preconditions, postconditions, main success scenario, alternate flow |
| [`Problem_Statement_24.pdf`](1-RE/Problem_Statement_24.pdf) | Original problem statement |

![Use-case diagram](1-RE/UseCase_Diagram.png)

## 2. Architecture — [`2-Architecture/`](2-Architecture/README.md)
![Architecture](2-Architecture/architecture.png)

## 3. Project creation screenshots — [`3-Project-Creation-Screenshots/`](3-Project-Creation-Screenshots/README.md)
Jira spaces `Kanban_BPS#24`, `Scrum_BPS#24` and `BugTracker_BPS#24`, with an index of every screenshot and its report PDF. GitHub creation screenshots go in `github/`.

## 4. SRS and WBS — [`4-SRS-and-WBS/`](4-SRS-and-WBS/)
- [`SRS.md`](4-SRS-and-WBS/SRS.md) — Software Requirements Specification
- [`WBS.md`](4-SRS-and-WBS/WBS.md) — Work Breakdown Structure mapped to Jira epics, stories, tasks and sprint

## 5. GitHub Copilot generated code — [`5-Copilot-Code/`](5-Copilot-Code/README.md)
Pending: screenshots or repository link will be added here.

## 6. Practising software testing tools — [`6-Testing-Tools/`](6-Testing-Tools/README.md)
Pending: testing process, bug fix and repository link will be added here.
