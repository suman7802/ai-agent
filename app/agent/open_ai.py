from openai import OpenAI
from app.configs import config


client = OpenAI(
    api_key=config["GEMINI"]["GEMINI_API_KEY"],
    base_url=config["OPENAI"]["BASE_URL"],
)
