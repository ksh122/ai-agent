from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


if __name__ == "__main__":

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )

    # load the model
    model = os.getenv("MODEL")

    # generate the response
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
