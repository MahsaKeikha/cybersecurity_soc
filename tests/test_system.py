from orchestration.orchestrator import SOCOrchestrator

def test_run():
    result = SOCOrchestrator().run({})
    assert result["system_id"] == "F45"
    assert "human" in result["human_authority"].lower()

def test_critical_alert_requires_review():
    case = {"alerts": [{"severity": "critical"}]}
    assert SOCOrchestrator().run(case)["status"] == "review_required"
