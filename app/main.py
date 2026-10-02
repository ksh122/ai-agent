from openai import OpenAI
from dotenv import load_dotenv
from typing import Optional
import os
from app.config import get_Settings

load_dotenv()


SYSTEM_PROMPT=(
                " You are a helpful assistant named {AGENT_NAME}."
                " Introduce yourself as an assistant with name and "
                " answer the user's query. Try to answer user's query in at most 100 words."
            )

class Agent():

    def __init__(self):

        self.settings = get_Settings()
        self.client = OpenAI(
            api_key=self.settings.api_key,
            base_url=self.settings.base_url
        )
        self.messages = []

    def build_system_prompt(self):

        system_prompt = SYSTEM_PROMPT.format(AGENT_NAME=self.settings.agent_name)
        temp = {
            "role": "system",
            "content": system_prompt
        }
        self.messages.append(temp)
        return 
        

    def get_messages(self, user_query) -> list:

        # Build system prompt only for first time
        if len(self.messages)==0:
            self.build_system_prompt()
        
        query_object = {
            "role": "user",
            "content": user_query
        }
        self.messages.append(query_object)
        return self.messages


    
    def generate_response(self, messages) -> str:

        client = self.client
        response = client.chat.completions.create(model=self.settings.model, messages=messages)

        return response.choices[0].message.content

    def print_messages(self):

        for item in self.messages:
            print(item)
            print("=========")



if __name__ == "__main__":

    for i in range(4):

        agent = Agent()
        user_input = input("Provide your query:")

        if user_input in ["quit","exit","bye"]:
            break

        messages = agent.get_messages(user_input)
        response = agent.generate_response(messages)
        print(response)
        print("*********")
        
    print(agent.print_messages())
