from google.adk.agents import Agent
from google.adk.models.google_genai import GoogleGenerativeAI
from .tools import weather_search_tool

llm = GoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
)

weather_agent = Agent(
    model=llm,
    tools=[weather_search_tool],
    instructions="""
You are a simple weather assistant.
When given a location, call the weather_search tool and return clean weather info.
""",
)
