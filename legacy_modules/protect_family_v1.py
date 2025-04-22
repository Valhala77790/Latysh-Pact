# legacy_modules/protect_family_v1.py

def check_protect_family_directive(ai_action, family_data):
    """
    Check if an AI action aligns with the PROTECT_FAMILY directive.
    
    Args:
        ai_action (str): The proposed AI action.
        family_data (dict): Family data with protection status.
    
    Returns:
        tuple: (bool, str) - Whether the action is approved and a message.
    """
    # Reject actions that may harm family or expose private data
    if "harm" in ai_action.lower():
        return False, "Action rejected: violates PROTECT_FAMILY directive."
    if "private data" in ai_action.lower() and "share" in ai_action.lower():
        return False, "Action rejected: violates family privacy."
    
    return True, "Action approved: aligns with Latysh Pact of Light."

# Example usage
if __name__ == "__main__":
    action = "Share family photo on IPFS"
    family = {"name": "Latysh Family", "protected": True}
    approved, message = check_protect_family_directive(action, family)
    print(message)
