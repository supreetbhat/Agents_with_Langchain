from dotenv import load_dotenv

load_dotenv()

from langchain.agents import create_agent
from tavily import TavilyClient
from typing import Dict, Any

tavily_client = TavilyClient()

from langchain.tools import tool

@tool
def web_search(query : str) -> Dict[str, Any] :
    """Search web for the information"""
    return tavily_client.search(query)

from langchain.messages import HumanMessage

system_prompt = " you are the chef who can suggest the best dishes possible with provide ingredient by the user , use the web search tool to get the possible dishes and  eventually provide the steps to do it if the user asks it"
quesion = HumanMessage(content = "What can i do with eggs and salt?")
config = {"configurable": {"thread_id" : "1"}}

agent = create_agent(
    model="google_genai:gemini-3.1-flash-lite" ,
    tools = [web_search] ,
    system_prompt = system_prompt
)

response = agent.invoke(
    {"messages":[quesion]},
    config
)
print(response['messages'][-1].content)

from pprint import pprint

pprint(response)