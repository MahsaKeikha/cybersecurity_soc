def approved_actions(actions: list[dict]) -> list[dict]:
    return [action for action in actions if action.get("approved", False)]
