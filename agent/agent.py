from google.adk.agents import Agent
from google.adk.models.google_llm import GoogleLLM
from .tools import weather_search_tool

# LLM: Gemini FlashLite 2
llm = GoogleLLM(model_name="gemini-2.0-flash-lite")

weather_agent = Agent(
    model=llm,
    tools=[weather_search_tool],
    instructions="""
You are a simple weather assistant.
Given a location, always search online and return clean, short weather details.
""",
)
