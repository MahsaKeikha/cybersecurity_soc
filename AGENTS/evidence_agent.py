class EvidenceAgent:
    name = "evidence"
    def run(self, case: dict) -> dict:
        evidence = case.get("evidence", [])
        missing = case.get("missing_evidence", [])
        return {"agent": self.name, "evidence": evidence, "missing": missing}
