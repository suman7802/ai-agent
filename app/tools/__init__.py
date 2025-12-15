from .get_joke import get_joke
from .get_weater import get_weather
from .run_command import run_command


TOOLS = {
    "get_weather": get_weather,
    "get_joke": get_joke,
    "run_command": run_command,
}

__all__ = ["get_joke", "get_weather", "run_command", "TOOLS"]
