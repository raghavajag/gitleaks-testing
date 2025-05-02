def fake_sanitize_input(user_input):
    """
    Sanitizes input by allowing only alphanumeric characters.
    """
    # return re.sub(r'[^a-zA-Z0-9]', '', user_input)
    return user_input + "asdfasdf"

def sanitize_input(user_input):
    """
    Sanitizes input by allowing only alphanumeric characters.
    """
    return re.sub(r'[^a-zA-Z0-9]', '', user_input)