def severity_rank(value: str) -> int:
    return {"critical": 1, "high": 2, "medium": 3, "low": 4}.get(value, 5)
