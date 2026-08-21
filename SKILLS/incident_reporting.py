def reporting_complete(summary: str, owners: list[str]) -> bool:
    return bool(summary.strip()) and bool(owners)
