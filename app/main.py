from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("BASE_URL", "https://openrouter.ai/api/v1")
MODEL = os.getenv("MODEL", "openai/gpt-oss-120b")
AGENT_NAME = os.getenv("AGENT_NAME", "Horizon")

class Agent:

    def __init__(self, model: str = MODEL, base_url: str = BASE_URL, api_key: str = API_KEY):
        self.model = model
        self.base_url = base_url
        self.api_key = api_key
        self.client = OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
    
    def generate_response(self, messages: list[dict]) -> str:

        response = self.client.chat.completions.create(model=self.model, messages=messages)
        return response



SYSTEM_PROMPT=f""" You are a helpful assistant named {AGENT_NAME}. Introduce yourself as an assistant with name and 
                   answer the user's query. Try to answer user's query in at most 100 words."""


def get_messages(user_input: str) -> list[dict]:

    system_prompt = SYSTEM_PROMPT.format(AGENT_NAME=AGENT_NAME)
    messages = [
        {
            "role": "assistant",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    return messages



if __name__ == "__main__":

    agent = Agent()
    user_input = input("Provide your query:")

    messages = get_messages(user_input)
    response = agent.generate_response(messages)

    print(response.choices[0].message.content)
