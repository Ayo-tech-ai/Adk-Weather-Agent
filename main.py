import streamlit as st
import uuid

st.set_page_config(page_title="Weather Agent", page_icon="⛅")
st.title("🌦️ Weather Agent")

# Initialize once
if 'runner' not in st.session_state:
    try:
        from google.adk.sessions import InMemorySessionService
        from google.adk.runners import Runner
        from agent.agent import weather_agent
        
        session_service = InMemorySessionService()
        session = session_service.create_session(
            app_name="weather-app",
            user_id=str(uuid.uuid4())
        )
        
        st.session_state.runner = Runner(
            agent=weather_agent,
            session=session
        )
    except Exception as e:
        st.error(f"Setup failed: {str(e)}")
        st.stop()

# Main interface
location = st.text_input("📍 Enter location:", placeholder="e.g., Lagos, Tokyo, London")

if st.button("Get Weather") and location:
    with st.spinner("🌤️ Fetching weather..."):
        try:
            response = st.session_state.runner.run(
                input_text=f"What's the current weather in {location}? Include temperature, conditions, and any important alerts."
            )
            
            st.success("✅ Weather Found!")
            st.write(response.output_text)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
