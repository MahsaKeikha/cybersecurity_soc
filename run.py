import json
from orchestration.orchestrator import SOCOrchestrator
if __name__ == "__main__":
    print(json.dumps(SOCOrchestrator().run({"alerts": [], "evidence": [], "missing_evidence": []}), indent=2))
