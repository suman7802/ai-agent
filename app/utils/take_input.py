def take_input(optional_message: str = None):
    """
    Docstring for take_input

    :param optional_message: Description
    :type optional_message: str
    """

    if optional_message:
        print(optional_message)

    user_query = input("> ")

    if user_query.lower() in ["exit", "quit"]:
        return

    return user_query
