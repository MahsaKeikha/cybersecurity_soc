class ReportingAgent:
    name = "reporting"
    def run(self, case: dict) -> dict:
        return {"agent": self.name, "summary": case.get("summary", "SOC review prepared"), "notifications": case.get("notifications", [])}
