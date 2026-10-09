from langchain_core.messages import AnyMessage, HumanMessage, SystemMessage, ToolMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from app.config import get_Settings
from app.main import Agent
from langchain.tools import tool
from langchain.chat_models import init_chat_model
from typing import Literal, TypedDict, Annotated
from app.prompts.system_prompt import SYSTEM_PROMPT
import operator
from app.prompts import system_prompt

@tool
def magic_operation(a:int, b:int)-> int:
    """
    Provides a result for 2 integer with a magical algorithm

    Args: 
        a: First integer
        b: Second integer
    """
    print(f"magic operation tool calles for {a} and {b}")
    result = (a**b ) * 2
    return result

tools = [magic_operation]
tools_by_name = {tool.name:tool for tool in tools}

class MessageState(TypedDict):

    messages: Annotated[list[AnyMessage], add_messages]


def agent_node(state:MessageState)-> MessageState:

    agent = Agent()
    system_prompt = SYSTEM_PROMPT.format(AGENT_NAME=agent.settings.agent_name)

    current_messages = list(state["messages"])
    if not current_messages or not isinstance(current_messages[0],SystemMessage):
        current_messages.insert(0,SystemMessage(content=system_prompt))


    model = agent.get_chat_model()
    model_with_tool = model.bind_tools(tools)
    result = model_with_tool.invoke(current_messages)
    
    return {"messages": [result]}
    

def tool_node(state: MessageState):

    result=[]

    for tool_call in getattr(state["messages"][-1], "tool_calls", []):
        tool = tools_by_name[tool_call["name"]]
        observation= tool.invoke(tool_call["args"])
        result.append(ToolMessage(content=observation, tool_call_id=tool_call["id"] ))


    return {"messages": result}


def should_continue(state: MessageState) -> Literal[END,"tool_node"]:

    last_message = state["messages"][-1]
    if getattr(last_message,"tool_calls",[]):
        return "tool_node"
    return END 







if __name__== "__main__":

    # agent = Agent()

    # model = agent.get_chat_model()

    # tools = [magic_operation]
    # tools_by_name = {tool.name:tool for tool in tools}
    # model_with_tool = model.bind_tools(tools)
    # print(tools_by_name)
    # # print("===============")
    # print(model_with_tool)

    # print(model_with_tool.invoke("Provide result for 2 and 3 by magical algorithm"))

    graph = StateGraph(MessageState)

    graph.add_node("agent_node", agent_node)
    graph.add_node("tool_node", tool_node)

    graph.add_edge(START, "agent_node")
    graph.add_conditional_edges("agent_node", should_continue, ["tool_node", END])
    graph.add_edge("tool_node","agent_node")

    workflow = graph.compile() 

    query = input("Provide your user query")
    initial_state = {
        "messages": [HumanMessage(content=query)]
    }

    final_state= workflow.invoke(initial_state)
    print(final_state)


    # from IPython.display import Image, display
    # # Show the agent
    # display(Image(workflow.get_graph(xray=True).draw_mermaid_png()))

