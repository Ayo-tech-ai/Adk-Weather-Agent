import streamlit as st
import uuid

st.set_page_config(page_title="Weather Agent", page_icon="⛅")
st.title("🌦️ Simple Weather Agent (Google ADK)")
st.write("Enter any location and I will fetch the current weather using Google Search.")

# Generate a unique session ID for each user
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

location = st.text_input("Enter a location:", "Lagos")

if st.button("Get Weather"):
    if not location.strip():
        st.error("Please enter a valid location.")
    else:
        with st.spinner(f"Searching for weather in {location}..."):
            try:
                # Import inside try block
                from google.adk.sessions import InMemorySessionService
                from google.adk.runners import Runner
                from agent.agent import weather_agent
                
                # Create session service
                session_service = InMemorySessionService()
                
                # Create session with required parameters
                session = session_service.create_session(
                    app_name="weather-agent-app",
                    user_id=st.session_state.session_id
                )
                
                # Create and run the runner
                runner = Runner(
                    agent=weather_agent,
                    session=session
                )
                
                # Run the agent
                response = runner.run(
                    input_text=f"Get the current weather for {location}. Include temperature, conditions, humidity, and wind speed."
                )
                
                # Display the response
                st.subheader(f"🌤️ Weather in {location}")
                st.write(response.output_text)
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.code(f"Full error: {str(e)}")
