from langchain_core.messages import HumanMessage
from lanchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()


def main():
    model = ChatOpenAI(model_name="gpt-4", temperature=0)

    tools = []
    agent_executor = create_react_agent(model=model, tools=tools)

    print("Welcome to the React Agent! Type 'exit' to quit.")
    print("You can ask questions or give commands to the agent.")
    print("For example, you can ask about the weather, get definitions, or perform calculations.")

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit":
            print("Exiting the React Agent. Goodbye!")
            break
        print("\nAssistant: ", end="")
        for chunk in agent_executor.stream({"messages": [HumanMessage(content=user_input)]}
                                           ):
            if "agent" in chunk and "message" in chunk["agent"]:
                for message in chunk["agent"]["message"]:
                    print(message.content, end="", flush=True)
        print()


if __name__ == "__main__":
    main()
