import streamlit as st

st.set_page_config(page_title="Weather Agent", page_icon="⛅")
st.title("🌦️ Weather Agent")

try:
    # Import
    from google.adk.sessions import InMemorySessionService
    from google.adk.runners import Runner
    from agent.agent import weather_agent
    
    # Setup runner (once)
    if 'runner' not in st.session_state:
        session_service = InMemorySessionService()
        st.session_state.runner = Runner(
            agent=weather_agent,
            app_name="weather_app",
            session_service=session_service
        )
    
    # User input
    location = st.text_input("Location:", "Lagos")
    
    if st.button("Get Weather"):
        # Just pass the query as a string, no keyword argument
        response = st.session_state.runner.run(
            f"What is the current weather in {location}?"
        )
        
        st.write("### 🌤️ Weather Result")
        st.write(response.output_text)
        
except Exception as e:
    st.error(f"Error: {str(e)}")
