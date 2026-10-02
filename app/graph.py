from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated
from app.main import Agent

class AgentState(BaseModel):

    query = Annotated[str, Field(description="User's query")]
    messages = list(Annotated[dict(str,str), Field(description="System prompt + Previous Context")])


def agent_node(state: AgentState)-> AgentState :

    llm = Agent()


