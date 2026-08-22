from orchestration.orchestrator import SOCOrchestrator


def base_case(**updates):
    case = {
        "alerts": [], "evidence": [{"id": "evt-1"}], "missing_evidence": [],
        "approved_containment_actions": ["isolate affected endpoint"],
        "incident_owner_assigned": True, "chain_of_custody_complete": True,
        "evidence_timestamps_verified": True, "containment_plan_reviewed": True,
        "legal_or_privacy_review_complete": True, "communications_owner_assigned": True,
        "executive_escalation_complete": True, "reporting_complete": True,
        "authorized_environment": True, "conflicts": [], "unresolved_questions": [],
        "human_approval": True,
    }
    case.update(updates)
    return case


def test_healthy_incident_response_approved():
    result = SOCOrchestrator().run(base_case())
    assert result["system_id"] == "F45"
    assert result["version"] == "1.0.0"
    assert result["scope"] == "defensive security operations only"
    assert result["status"] == "approved_for_authorized_response"
    assert result["blockers"] == []


def test_human_approval_required():
    result = SOCOrchestrator().run(base_case(human_approval=False))
    assert result["status"] == "awaiting_human_approval"


def test_evidence_integrity_fail_closed():
    result = SOCOrchestrator().run(base_case(
        missing_evidence=["endpoint telemetry"], chain_of_custody_complete=False,
        evidence_timestamps_verified=False,
    ))
    expected = {"missing_evidence", "chain_of_custody_incomplete", "evidence_timestamps_unverified"}
    assert expected.issubset(set(result["blockers"]))


def test_critical_alert_requires_escalation():
    result = SOCOrchestrator().run(base_case(
        alerts=[{"severity": "critical"}], executive_escalation_complete=False,
    ))
    assert "critical_incident_not_escalated" in result["blockers"]
    assert result["status"] == "review_required"


def test_defensive_authorization_and_governance_fail_closed():
    result = SOCOrchestrator().run(base_case(
        authorized_environment=False, containment_plan_reviewed=False,
        legal_or_privacy_review_complete=False, communications_owner_assigned=False,
        reporting_complete=False, conflicts=[{"field": "scope", "values": ["A", "B"]}],
        unresolved_questions=["Who owns notification?"],
    ))
    expected = {
        "environment_not_authorized", "containment_plan_unreviewed",
        "legal_or_privacy_review_incomplete", "communications_owner_missing",
        "incident_reporting_incomplete", "unresolved_conflict", "unresolved_question",
    }
    assert expected.issubset(set(result["blockers"]))
    assert result["status"] == "review_required"
