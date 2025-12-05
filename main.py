import streamlit as st
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from agent.agent import weather_agent

st.set_page_config(page_title="Weather Agent", page_icon="⛅")

st.title("🌦️ Simple Weather Agent (Google ADK)")
st.write("Enter any location and I will fetch the current weather using Google Search.")

location = st.text_input("Enter a location:")

if st.button("Get Weather"):
    if not location.strip():
        st.error("Please enter a valid location.")
    else:
        with st.spinner("Searching..."):
            try:
                # Create session and runner
                session_service = InMemorySessionService()
                session = session_service.create_session()
                
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
                st.info("Check if GOOGLE_API_KEY is set in Streamlit Secrets")
