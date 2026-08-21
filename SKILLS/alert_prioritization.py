def highest_severity(alerts: list[dict]) -> str:
    order = ["critical", "high", "medium", "low"]
    values = {a.get("severity") for a in alerts}
    return next((value for value in order if value in values), "none")
