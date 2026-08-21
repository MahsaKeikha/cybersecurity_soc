class ContainmentPlanningAgent:
    name = "containment_planning"
    def run(self, case: dict) -> dict:
        actions = case.get("approved_containment_actions", [])
        return {"agent": self.name, "approved_actions": actions, "human_approval_required": True}
