from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

model = os.getenv("MODEL")

response = client.chat.completions.create(
    model= model,
    messages=[
        {
            "role": "user",
            "content": "Explain LangGraph in simple terms"
        }
    ]
)

print(response.choices[0].message.content)