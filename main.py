import streamlit as st
import uuid

st.set_page_config(page_title="Weather Agent", page_icon="⛅")
st.title("🌦️ Weather Agent with Session")

# Setup runner
if 'runner' not in st.session_state:
    try:
        from google.adk.sessions import InMemorySessionService
        from google.adk.runners import Runner
        from agent.agent import weather_agent
        
        session_service = InMemorySessionService()
        runner = Runner(
            agent=weather_agent,
            app_name="weather_app",
            session_service=session_service
        )
        
        st.session_state.runner = runner
        st.session_state.session_service = session_service
        st.session_state.user_id = str(uuid.uuid4())
        
        st.success("✅ System ready!")
        
    except Exception as e:
        st.error(f"Setup failed: {str(e)}")
        st.stop()

# Create session for this user
if 'session' not in st.session_state:
    try:
        session = st.session_state.session_service.create_session(
            app_name="weather_session",
            user_id=st.session_state.user_id
        )
        st.session_state.session = session
    except Exception as e:
        st.error(f"Session creation failed: {str(e)}")

# Main app
location = st.text_input("Enter location:", "Lagos")

if st.button("Get Weather"):
    if not location:
        st.warning("Please enter a location")
    else:
        with st.spinner("Searching..."):
            try:
                # Two possible ways - try both
                try:
                    # Method 1: Direct runner.run() with query
                    response = st.session_state.runner.run(
                        f"Get current weather for {location}"
                    )
                except Exception as e1:
                    # Method 2: Try with session parameter
                    response = st.session_state.runner.run(
                        f"Get current weather for {location}",
                        session=st.session_state.session
                    )
                
                st.subheader(f"🌤️ Weather in {location}")
                st.write(response.output_text)
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
