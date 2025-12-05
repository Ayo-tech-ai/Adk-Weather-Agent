import streamlit as st
import uuid

st.set_page_config(page_title="Weather Agent", page_icon="⛅")
st.title("🌦️ Simple Weather Agent")

# Initialize once
if 'runner' not in st.session_state:
    try:
        from google.adk.sessions import InMemorySessionService
        from google.adk.runners import Runner
        from agent.agent import weather_agent
        
        # Create session service
        session_service = InMemorySessionService()
        
        # Create runner with session_service, not session
        st.session_state.runner = Runner(
            agent=weather_agent,
            session_service=session_service,
            app_name="weather-app"
        )
        
        st.success("✅ Agent initialized successfully!")
    except Exception as e:
        st.error(f"Setup failed: {str(e)}")
        st.code(f"Error details: {str(e)}")

# Main interface
st.write("Enter a location to get current weather information:")

location = st.text_input("📍 Location:", placeholder="e.g., Lagos, Tokyo, London")

if st.button("Get Weather") and location:
    with st.spinner("🌤️ Fetching weather..."):
        try:
            response = st.session_state.runner.run(
                input_text=f"What's the current weather in {location}? Include temperature, conditions, humidity, wind speed, and any important alerts."
            )
            
            st.success("✅ Weather Found!")
            st.write(response.output_text)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
