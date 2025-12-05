import streamlit as st

st.set_page_config(page_title="Weather Agent", page_icon="⛅")
st.title("🌦️ Simple Weather Agent")

# Initialize runner
if 'runner' not in st.session_state:
    try:
        from google.adk.sessions import InMemorySessionService
        from google.adk.runners import Runner
        from agent.agent import weather_agent
        
        # Setup runner exactly like your working example
        session_service = InMemorySessionService()
        runner = Runner(
            agent=weather_agent,
            app_name="weather_agent_app",
            session_service=session_service
        )
        
        st.session_state.runner = runner
        st.success("✅ Agent initialized!")
        
    except Exception as e:
        st.error(f"Setup failed: {str(e)}")
        st.stop()

# Main interface
st.write("Enter a location to get current weather information:")

location = st.text_input("📍 Location:", placeholder="e.g., Lagos, Tokyo, London")

if st.button("Get Weather") and location:
    with st.spinner("🌤️ Fetching weather..."):
        try:
            # Call runner.run() with the query as positional argument
            # NOT as keyword argument 'input_text='
            response = st.session_state.runner.run(
                f"What's the current weather in {location}? Include temperature, conditions, humidity, wind speed."
            )
            
            st.success("✅ Weather Found!")
            st.write(response.output_text)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
