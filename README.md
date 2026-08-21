# F45 Cybersecurity SOC

Standalone multi-agent reference implementation for defensive security operations, alert triage, evidence handling, incident coordination, containment planning, and reporting.

## Direct agent links

- [Alert Triage Agent](AGENTS/alert_triage_agent.py)
- [Evidence Agent](AGENTS/evidence_agent.py)
- [Incident Coordination Agent](AGENTS/incident_coordination_agent.py)
- [Containment Planning Agent](AGENTS/containment_planning_agent.py)
- [Reporting Agent](AGENTS/reporting_agent.py)

## Core implementation

- [All agents](AGENTS/)
- [All tools](TOOLS/)
- [All skills](SKILLS/)
- [Orchestration](orchestration/)
- [Tests](tests/)

## Execution

```bash
python run.py
pytest -q
```

This repository is defensive and educational. It does not provide offensive intrusion automation.
