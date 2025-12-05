# For ADK 1.20.0, Google Search tool is in a different location
try:
    # Try the new location first
    from google.adk.tools.google_search_tool import GoogleSearchTool
except ImportError:
    # Fallback to alternative import
    try:
        from google.adk.tools import GoogleSearchTool
    except ImportError:
        # Last resort - create a simple function
        import requests
        import os
        
        def google_search_tool(query: str):
            """Fallback search function"""
            # This is a placeholder - you'd need to implement actual search
            return f"Search for: {query}"
        
        GoogleSearchTool = type('GoogleSearchTool', (), {
            '__call__': lambda self, query: google_search_tool(query),
            'name': 'weather_search',
            'description': 'Search for weather information'
        })

# Create the tool instance
weather_search_tool = GoogleSearchTool(
    name="weather_search",
    description="Search the internet for current weather information for any location."
)
