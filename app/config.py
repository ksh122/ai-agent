from dotenv import load_dotenv
import os

load_dotenv()


class Settings():

    def __init__(self):

        API_KEY = os.getenv("OPENAI_API_KEY")
        BASE_URL = os.getenv("BASE_URL", "https://openrouter.ai/api/v1")
        MODEL = os.getenv("MODEL", "openai/gpt-oss-120b")
        AGENT_NAME = os.getenv("AGENT_NAME", "Horizon")
