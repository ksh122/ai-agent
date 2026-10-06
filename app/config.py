from dotenv import load_dotenv
import os
from functools import lru_cache

load_dotenv()


class Settings():

    def __init__(self):

        self.api_key = os.getenv("API_KEY")
        self.base_url = os.getenv("BASE_URL", "https://openrouter.ai/api/v1")
        self.model = os.getenv("MODEL", "openai/gpt-oss-120b")
        self.agent_name = os.getenv("AGENT_NAME", "Horizon")
        self.max_tokens = os.getenv("MAX_TOKENS",2048)
        self.model_provider = os.getenv("MODEL_PROVIDER","openrouter")

@lru_cache
def get_Settings() -> Settings:
    "Cached Settings config"
    return Settings()