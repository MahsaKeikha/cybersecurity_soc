from __future__ import annotations

from copy import deepcopy

from AGENTS.alert_triage_agent import AlertTriageAgent
from AGENTS.containment_planning_agent import ContainmentPlanningAgent
from AGENTS.evidence_agent import EvidenceAgent
from AGENTS.incident_coordination_agent import IncidentCoordinationAgent
from AGENTS.reporting_agent import ReportingAgent


class SOCOrchestrator:
    """Defensive, fail-closed SOC incident governance for F45."""

    def __init__(self):
        self.agents = [
            AlertTriageAgent(),
            EvidenceAgent(),
            IncidentCoordinationAgent(),
            ContainmentPlanningAgent(),
            ReportingAgent(),
        ]

    def run(self, case: dict) -> dict:
        state = self._normalize(case)
        analyses, trace = {}, []
        for step, agent in enumerate(self.agents, 1):
            analyses[agent.name] = agent.run(state)
            trace.append({"step": step, "actor": agent.name, "event": "completed"})

        blockers = self._blockers(state, analyses)
        if blockers:
            status = "review_required"
        elif state["human_approval"]:
            status = "approved_for_authorized_response"
        else:
            status = "awaiting_human_approval"
        trace.append({"step": len(trace) + 1, "actor": "soc_authorization_gate", "event": status, "blockers": blockers})

        return {
            "system_id": "F45",
            "system_name": "Cybersecurity SOC",
            "version": "1.0.0",
            "maturity": "L3 Gold Standard",
            "scope": "defensive security operations only",
            "state": state,
            "analyses": analyses,
            "blockers": blockers,
            "ready_for_approval": not blockers,
            "status": status,
            "human_authority": "Containment and response actions require authorized human approval",
            "trace": trace,
        }

    @staticmethod
    def _normalize(case: dict) -> dict:
        state = deepcopy(case)
        for key in (
            "alerts", "evidence", "missing_evidence", "approved_containment_actions",
            "conflicts", "unresolved_questions", "open_risks",
        ):
            state.setdefault(key, [])
        state.setdefault("human_approval", False)
        state.setdefault("incident_owner_assigned", False)
        state.setdefault("chain_of_custody_complete", False)
        state.setdefault("evidence_timestamps_verified", False)
        state.setdefault("containment_plan_reviewed", False)
        state.setdefault("legal_or_privacy_review_complete", True)
        state.setdefault("communications_owner_assigned", False)
        state.setdefault("executive_escalation_complete", False)
        state.setdefault("reporting_complete", False)
        state.setdefault("authorized_environment", True)
        return state

    @staticmethod
    def _blockers(state: dict, analyses: dict) -> list[str]:
        blockers: list[str] = []
        if not state["authorized_environment"]:
            blockers.append("environment_not_authorized")
        if analyses["evidence"]["missing"]:
            blockers.append("missing_evidence")
        if not state["chain_of_custody_complete"]:
            blockers.append("chain_of_custody_incomplete")
        if not state["evidence_timestamps_verified"]:
            blockers.append("evidence_timestamps_unverified")
        if not state["incident_owner_assigned"]:
            blockers.append("incident_owner_missing")
        if not state["containment_plan_reviewed"]:
            blockers.append("containment_plan_unreviewed")
        if not state["legal_or_privacy_review_complete"]:
            blockers.append("legal_or_privacy_review_incomplete")
        if not state["communications_owner_assigned"]:
            blockers.append("communications_owner_missing")
        critical = analyses["alert_triage"].get("critical", [])
        if critical and not state["executive_escalation_complete"]:
            blockers.append("critical_incident_not_escalated")
        if not state["reporting_complete"]:
            blockers.append("incident_reporting_incomplete")
        if state["conflicts"]:
            blockers.append("unresolved_conflict")
        if state["unresolved_questions"]:
            blockers.append("unresolved_question")
        return blockers
