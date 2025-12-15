import requests


def get_weather(city: str) -> str:
    """
    Fetch current weather for a given city.
    """
    try:
        url = f"https://wttr.in/{city.lower()}?format=%C%t"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.text.strip()
        return "Unable to fetch weather data at the moment."
    except Exception:
        return "Error fetching weather data."
