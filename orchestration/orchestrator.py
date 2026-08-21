from AGENTS.alert_triage_agent import AlertTriageAgent
from AGENTS.evidence_agent import EvidenceAgent
from AGENTS.incident_coordination_agent import IncidentCoordinationAgent
from AGENTS.containment_planning_agent import ContainmentPlanningAgent
from AGENTS.reporting_agent import ReportingAgent

class SOCOrchestrator:
    def __init__(self):
        self.agents = [AlertTriageAgent(), EvidenceAgent(), IncidentCoordinationAgent(), ContainmentPlanningAgent(), ReportingAgent()]
    def run(self, case: dict) -> dict:
        analyses, trace = {}, []
        for step, agent in enumerate(self.agents, 1):
            analyses[agent.name] = agent.run(case)
            trace.append({"step": step, "actor": agent.name, "event": "completed"})
        review = bool(analyses["alert_triage"]["critical"] or analyses["evidence"]["missing"])
        return {"system_id": "F45", "system_name": "Cybersecurity SOC", "version": "0.1.0", "analyses": analyses, "status": "review_required" if review else "complete", "human_authority": "Containment actions require authorized human approval", "trace": trace}
