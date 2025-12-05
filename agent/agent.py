import os
from google.adk.agents import Agent
from google.adk.models.google_llm import Gemini
from .tools import weather_search_tool

# Create weather agent using the correct Gemini model class
weather_agent = Agent(
    name="weather_agent",
    model=Gemini(model="gemini-2.0-flash-lite"),
    instruction="""You are a weather assistant. Given a location:
1. Search for current weather information using Google Search
2. Return temperature, conditions, humidity, wind speed
3. Include any weather advisories or warnings
4. Format response clearly and concisely
5. Focus on accuracy and practical information""",
    tools=[weather_search_tool],
    output_key="weather_result"
)
