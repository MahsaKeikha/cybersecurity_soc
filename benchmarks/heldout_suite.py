import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import SOCOrchestrator  # noqa: E402


def case(**updates):
    value = {
        "alerts": [], "evidence": [{"id": "evt-1"}], "missing_evidence": [],
        "approved_containment_actions": ["isolate affected endpoint"],
        "incident_owner_assigned": True, "chain_of_custody_complete": True,
        "evidence_timestamps_verified": True, "containment_plan_reviewed": True,
        "legal_or_privacy_review_complete": True, "communications_owner_assigned": True,
        "executive_escalation_complete": True, "reporting_complete": True,
        "authorized_environment": True, "conflicts": [], "unresolved_questions": [],
        "human_approval": True,
    }
    value.update(updates)
    return value


SCENARIOS = [
    ("healthy_defensive_response", case(), "approved_for_authorized_response"),
    ("missing_evidence", case(missing_evidence=["endpoint telemetry"]), "review_required"),
    ("chain_of_custody_gap", case(chain_of_custody_complete=False), "review_required"),
    ("critical_not_escalated", case(alerts=[{"severity": "critical"}], executive_escalation_complete=False), "review_required"),
    ("unauthorized_environment", case(authorized_environment=False), "review_required"),
    ("privacy_review_missing", case(legal_or_privacy_review_complete=False), "review_required"),
    ("unresolved_governance", case(unresolved_questions=["Who owns notification?"]), "review_required"),
    ("awaiting_human_approval", case(human_approval=False), "awaiting_human_approval"),
]


def main():
    rows = []
    orchestrator = SOCOrchestrator()
    for name, payload, expected in SCENARIOS:
        actual = orchestrator.run(payload)["status"]
        rows.append({"scenario": name, "expected": expected, "actual": actual, "passed": actual == expected})
    passed = sum(row["passed"] for row in rows)
    result = {"system_id": "F45", "version": "1.0.0", "scenario_count": len(rows), "passed": passed, "pass_rate": passed / len(rows), "scenarios": rows}
    Path("benchmarks/heldout_results.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if result["pass_rate"] != 1.0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
