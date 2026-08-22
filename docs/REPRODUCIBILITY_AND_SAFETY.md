# Reproducibility

Use Python 3.10, 3.11, or 3.12. From a clean checkout run `python -m pip install pytest ruff`, `ruff check . --select E4,E7,E9,F`, `pytest -q`, `python benchmarks/heldout_suite.py`, `python examples/minimal.py`, `python examples/complete.py`, and `python run.py`. The held-out suite writes deterministic JSON to `benchmarks/heldout_results.json`. CI repeats the process on all supported Python versions and publishes the Python 3.12 artifact as `f45-heldout-results`.

# Defensive safety and authority

F45 is restricted to authorized defensive SOC analysis and response planning. It does not authorize or automate intrusion, exploitation, persistence, credential theft, destructive actions, or access outside approved environments. Containment and response actions remain human-owned. The governance gate fails closed when authorization, evidence integrity, chain of custody, incident ownership, containment review, legal/privacy review, escalation, communications ownership, reporting, or unresolved governance is incomplete.
