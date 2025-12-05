from google.adk.agents import Agent
from google.adk import agents
from google import genai
from .tools import weather_search_tool

# Initialize Gemini FlashLite 2 using the new API format
# ADK 1.20.0 has a different structure for models
client = genai.Client(api_key=None)  # Will use GOOGLE_API_KEY from environment

weather_agent = Agent(
    # Use the new model parameter format
    model="gemini-2.0-flash-lite",
    tools=[weather_search_tool],
    instructions="""
You are a simple weather assistant.
Given a location, always search online and return clean, short weather details.
Include:
1. Current temperature
2. Weather conditions (sunny, rainy, etc.)
3. Humidity if available
4. Wind speed if available
5. Any relevant advisories

Format the response in a clear, readable way.
""",
)
