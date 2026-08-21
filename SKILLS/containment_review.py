def containment_gate(human_approved: bool, actions: list[dict]) -> bool:
    return human_approved and bool(actions)
