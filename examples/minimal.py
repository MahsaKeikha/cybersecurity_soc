import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from orchestration.orchestrator import SOCOrchestrator  # noqa: E402

case = {
    "evidence": [{"id": "evt-1"}], "incident_owner_assigned": True,
    "chain_of_custody_complete": True, "evidence_timestamps_verified": True,
    "containment_plan_reviewed": True, "communications_owner_assigned": True,
    "reporting_complete": True, "authorized_environment": True,
    "human_approval": False,
}
result = SOCOrchestrator().run(case)
assert result["status"] == "awaiting_human_approval"
print(result["status"])
