from langgraph.graph import START, END, StateGraph
from typing import TypedDict


# Define the state schema
class BMIState(TypedDict):

    height: float
    weight: float
    bmi: float
    category: str

def calculate_bmi(State:BMIState) -> BMIState:

    bmi = State["weight"] / (State["height"] ** 2)
    State["bmi"] = round(bmi,2)
    return State


def label_bmi(State:BMIState) -> BMIState:

    if State["bmi"] < 18.5:
        State["category"] = "Underweight"
    elif State["bmi"] >= 18.5 and State["bmi"] < 25:
        State["category"] = "Normal weight"
    elif State["bmi"] >= 25 and State["bmi"] < 30:
        State["category"] = "Overweight"
    else:
        State["category"] = "Obesity"
    return State

# Define the graph
graph = StateGraph(BMIState)

# add nodes to the graph
graph.add_node("calculate_bmi", calculate_bmi)
graph.add_node("label_bmi", label_bmi)

# add edges to the graph
graph.add_edge(START, "calculate_bmi")
graph.add_edge("calculate_bmi", "label_bmi")
graph.add_edge("label_bmi", END)

# compile the graph
workflow = graph.compile()

if __name__ == "__main__":

    print("Welcome to the BMI Calculator")

    height = float(input("Enter your height in meters:"))
    weight = float(input("Enter your weight in kilograms:"))

    result = workflow.invoke({"height": height, "weight": weight})
    print(f"Your BMI is {result['bmi']} and you are {result['category']}")
