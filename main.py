import streamlit as st
import uuid
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from agent.agent import weather_agent

st.set_page_config(page_title="Weather Agent", page_icon="⛅")

st.title("🌦️ Simple Weather Agent (Google ADK)")
st.write("Enter any location and I will fetch the current weather using Google Search.")

# Generate a unique session ID for each user
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

location = st.text_input("Enter a location:")

if st.button("Get Weather"):
    if not location.strip():
        st.error("Please enter a valid location.")
    else:
        with st.spinner("Searching..."):
            try:
                # Create session service with required parameters
                session_service = InMemorySessionService()
                
                # Create session with required app_name and user_id
                session = session_service.create_session(
                    app_name="weather-agent-app",
                    user_id=st.session_state.session_id
                )
                
                # Create runner
                runner = Runner(
                    agents=[weather_agent],
                    session=session
                )
                
                # Run the agent
                response = runner.run(
                    input_text=f"Get the current weather for {location}.",
                    agent=weather_agent
                )
                
                # Display the response
                if hasattr(response, 'agent_responses'):
                    for agent_response in response.agent_responses:
                        if agent_response.agent_name == weather_agent.name:
                            st.subheader(f"🌤️ Weather in {location}")
                            st.write(agent_response.output_text)
                            break
                else:
                    st.write(response.output_text)
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.code(f"Full error: {str(e)}")
