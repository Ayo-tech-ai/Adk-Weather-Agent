import streamlit as st
import uuid

st.set_page_config(page_title="Weather Test", page_icon="⛅")
st.title("🌤️ Weather Test")

try:
    from google.adk.sessions import InMemorySessionService
    from google.adk.runners import Runner
    from agent.agent import weather_agent
    
    # Create runner
    session_service = InMemorySessionService()
    runner = Runner(
        agent=weather_agent,
        app_name="test-weather",
        session_service=session_service
    )
    
    # Generate IDs
    user_id = str(uuid.uuid4())
    session_id = str(uuid.uuid4())
    
    # Simple interface
    location = st.text_input("City:", "Lagos")
    
    if st.button("Test"):
        response = runner.run(
            user_id=user_id,
            session_id=session_id,
            new_message=f"Weather in {location}"
        )
        
        st.write("Result:", response.output_text)
        
except Exception as e:
    st.error(f"Error: {str(e)}")
