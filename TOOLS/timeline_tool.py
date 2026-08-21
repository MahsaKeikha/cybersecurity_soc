def ordered_events(events: list[dict]) -> list[dict]:
    return sorted(events, key=lambda item: item.get("timestamp", ""))
