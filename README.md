# F45 Cybersecurity SOC

**Maturity:** L3 Gold Standard candidate  
**Version:** 1.0.0

A reproducible, defensive-only multi-agent reference system for security operations. Five specialized agents cover alert triage, evidence assessment, incident coordination, containment planning, and reporting. The orchestration layer keeps response authority with authorized humans and fails closed when evidence integrity, ownership, legal/privacy review, escalation, reporting, or scope authorization is incomplete.

## Defensive scope

F45 is for authorized SOC analysis and incident-response planning. It does not provide intrusion, exploitation, persistence, credential theft, destructive action, or unauthorized access automation.

## Fail-closed incident governance

An incident response cannot be approved when the environment is unauthorized, required evidence is missing, chain of custody is incomplete, timestamps are unverified, no incident owner is assigned, containment has not been reviewed, legal/privacy review is incomplete, communications ownership is missing, a critical incident has not been escalated, reporting is incomplete, or governance conflicts/questions remain unresolved. Human approval is required after automated gates pass and cannot override blockers.

## Reproduce

```bash
python -m pip install pytest ruff
ruff check . --select E4,E7,E9,F
pytest -q
python benchmarks/heldout_suite.py
python examples/minimal.py
python examples/complete.py
python run.py
```

CI validates Python 3.10, 3.11, and 3.12 and publishes held-out results from Python 3.12.

## Structure

- `AGENTS/`: alert triage, evidence, coordination, containment planning, and reporting roles
- `SKILLS/`: reusable defensive SOC review policies
- `TOOLS/`: severity, evidence ledger, timeline, and containment-checklist utilities
- `orchestration/`: fail-closed authorization flow
- `benchmarks/`: held-out defensive reproducibility suite
- `examples/`: clean-checkout minimal and complete examples
- `tests/`: behavioral and adversarial governance gates
- `docs/`: architecture, safety, reproducibility, and L3 audit evidence

L3 denotes an independently reviewable and reproducible defensive reference implementation. It does not replace incident command, legal counsel, organizational authorization, evidence-handling policy, or human response authority.
