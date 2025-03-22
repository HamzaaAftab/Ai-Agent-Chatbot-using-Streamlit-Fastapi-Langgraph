import os 
from dotenv import load_dotenv

load_dotenv()

# Step1: Setup API Keys for GROQ and TAVILY

GROQ_API_KEY = os.environ.get('GROQ_API_KEY')
TAVILY_API_KEY = os.environ.get('TAVILY_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# Step2: Setup LLM and Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="qwen-2.5-32b")

search_tool = TavilySearchResults(max_results=3)

# Step3: Setup AI Agent with Search Tool Functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage

system_prompt = "Act as an AI Chatbot who is the Smartest Chatbot ever made, you should have the best and correct knowledge, therefore look for the correct and best knowledge. Act as you r the most intelligent, smartest Person who is capable to do any task and ability to answer any question. Besides this you should be Friendly."

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)
    
    tools = [TavilySearchResults(max_results=3)] if allow_search else []
    
    agent = create_react_agent(
    model=llm,
    tools=tools,
    state_modifier= system_prompt
)

    state= {"messages": query}
    response = agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    return (ai_messages[-1])



