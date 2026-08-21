class IncidentCoordinationAgent:
    name = "incident_coordination"
    def run(self, case: dict) -> dict:
        return {"agent": self.name, "incident_id": case.get("incident_id"), "owners": case.get("owners", []), "status": case.get("incident_status", "open")}
