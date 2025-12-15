import requests
from typing import Optional


def get_joke(_: Optional[str] = None) -> str:
    """
    Returns a random programming joke.
    """
    try:
        response = requests.get(
            "https://official-joke-api.appspot.com/jokes/programming/random",
            timeout=5,
        )
        if response.status_code == 200:
            joke = response.json()[0]
            return f"{joke['setup']} {joke['punchline']}"
        return "Unable to fetch joke at the moment."
    except Exception:
        return "Error fetching joke."
