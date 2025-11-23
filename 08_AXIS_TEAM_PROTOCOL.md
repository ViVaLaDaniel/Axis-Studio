\# AXIS STUDIOS: TEAM COLLABORATION PROTOCOL v1.0



\*\*OBJECTIVE:\*\* Standardize workflows for a scalable team (1-10 developers).



\## 🎭 ROLES \& RESPONSIBILITIES



| Role | Focus | Output | Tools |

| :--- | :--- | :--- | :--- |

| \*\*Strategist (CPO)\*\* | Market analysis, "Killer Features" | Concept Doc (File 02) | Google Trends, Brain |

| \*\*Architect\*\* | Structure, Data schema, Dependencies | JSON Templates (File 00) | VS Code, JSON Lint |

| \*\*Developer\*\* | Liquid, JS, CSS | Working Code (File 03) | Shopify CLI, Git |

| \*\*QA Engineer\*\* | Validation, Testing, Security | Bug Report (File 05/07) | Devices, Lighthouse |



\## 🤝 HANDOFF PROTOCOL



1\.  \*\*Strategy -> Architect:\*\*

&nbsp;   \* \*Input:\* "We need a Video Bento Grid."

&nbsp;   \* \*Deliverable:\* `sections/video-bento.liquid` (empty shell) + `schema` definition.



2\.  \*\*Architect -> Developer:\*\*

&nbsp;   \* \*Input:\* Schema and constraints.

&nbsp;   \* \*Deliverable:\* Functional JS/CSS logic.



3\.  \*\*Developer -> QA:\*\*

&nbsp;   \* \*Input:\* Pull Request (PR).

&nbsp;   \* \*Requirement:\* CI Tests (File 07) must be GREEN before human QA starts.



\## 🚨 EMERGENCY PROTOCOL (RED BUTTON)



If a critical bug hits Production (Live Site):

1\.  \*\*ROLLBACK:\*\* Run `git revert HEAD` immediately.

2\.  \*\*ISOLATE:\*\* Use `theme serve` locally to reproduce.

3\.  \*\*FIX:\*\* Commit via `hotfix/` branch.

4\.  \*\*POST-MORTEM:\*\* AI must analyze \*why\* File 07 missed this bug.

