def evidence_gaps(required: list[str], supplied: list[str]) -> list[str]:
    return sorted(set(required) - set(supplied))
