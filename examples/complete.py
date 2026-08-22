import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import SOCOrchestrator  # noqa: E402

case = {
    "alerts": [{"severity": "high"}], "evidence": [{"id": "evt-1"}], "missing_evidence": [],
    "approved_containment_actions": ["isolate affected endpoint"],
    "incident_owner_assigned": True, "chain_of_custody_complete": True,
    "evidence_timestamps_verified": True, "containment_plan_reviewed": True,
    "legal_or_privacy_review_complete": True, "communications_owner_assigned": True,
    "executive_escalation_complete": True, "reporting_complete": True,
    "authorized_environment": True, "conflicts": [], "unresolved_questions": [],
    "human_approval": True,
}
result = SOCOrchestrator().run(case)
assert result["status"] == "approved_for_authorized_response"
assert result["ready_for_approval"] is True
print(result["status"], result["blockers"])
