class AlertTriageAgent:
    name = "alert_triage"
    def run(self, case: dict) -> dict:
        alerts = case.get("alerts", [])
        critical = [a for a in alerts if a.get("severity") == "critical"]
        return {"agent": self.name, "alerts": alerts, "critical": critical}
