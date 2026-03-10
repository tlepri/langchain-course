from dotenv import load_dotenv

load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
#from langchain_tavily import TavilySearch  this is its own tool to be used as a tool

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """ 
    Tool that searches over internet
    Args:
        query: The query to serach for
    Returns:
        The search results
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)


llm = ChatOpenAI(model="gpt-4o-mini")
tools = [search]#
#tools = [TavilySearch()] this is its own tool to be used as a tool, using this delete @tool decorator and the search function 
agent = create_agent(model=llm, tools=tools)


def main():
    print("Hello from langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="search for 3 job postings for an ai engineer using langchain in toronto on linkedin and list thir details  ")})
    print(result)


if __name__ == "__main__":
    main()
