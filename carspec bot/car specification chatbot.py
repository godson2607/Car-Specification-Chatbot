import openai
from langgraph.graph import StateGraph
from typing import TypedDict
from openai import OpenAI

# Set your OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your actual key

# Define state for LangGraph
class CarSpecState(TypedDict):
    car_query: str
    result: str

# Function to query GPT-3.5 Turbo for car specs
def get_car_specs(state: CarSpecState) -> CarSpecState:
    car_query = state["car_query"]

    prompt = f"""
    You are an automotive expert. A user is asking for specifications of a car.
    Respond clearly and concisely with technical details like engine type, fuel efficiency, top speed, features, and price.
    
    User query: "{car_query}"

    Answer in a helpful and structured format.
    """

    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    answer = response.choices[0].message.content
    return {"car_query": car_query, "result": answer}

# Define the LangGraph structure
def create_graph():
    builder = StateGraph(CarSpecState)
    builder.add_node("get_specs", get_car_specs)
    builder.set_entry_point("get_specs")
    builder.set_finish_point("get_specs")
    return builder.compile()

# CLI chatbot loop
def main():
    graph = create_graph()
    print("🚗 Car Specification Chatbot (LangGraph + GPT-3.5)")
    print("Type 'exit' to quit.\n")

    while True:
        query = input("Ask about a car model (e.g., 'Tell me about Hyundai Ioniq 5'):\n> ")

        if query.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not query.strip():
            print("Please enter a valid car model.")
            continue

        result = graph.invoke({"car_query": query})
        print("\n📋 Car Specifications:\n")
        print(result["result"])
        print("\n---\n")

if __name__ == "__main__":
    main()
