from google.adk.tools.google_search import GoogleSearchTool

# Simple wrapper for the google search tool
weather_search_tool = GoogleSearchTool(
    name="weather_search",
    description="Search the internet for current weather information for any location."
)
