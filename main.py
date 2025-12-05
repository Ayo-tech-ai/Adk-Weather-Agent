import streamlit as st
import uuid

st.set_page_config(page_title="Weather Agent", page_icon="⛅")
st.title("🌦️ Weather Agent Debug")

# Check all imports work
st.write("### Testing Imports")
try:
    from google.adk.sessions import InMemorySessionService
    from google.adk.runners import Runner
    from agent.agent import weather_agent
    
    st.success("✅ All imports successful")
    
    # Check Runner parameters
    st.write("### Checking Runner Parameters")
    import inspect
    runner_params = inspect.signature(Runner.__init__).parameters
    st.write("Runner accepts:", list(runner_params.keys()))
    
    # Main app
    st.write("### Weather Search")
    
    if 'session_id' not in st.session_state:
        st.session_state.session_id = str(uuid.uuid4())
    
    location = st.text_input("Enter location:", "Lagos")
    
    if st.button("Test"):
        with st.spinner("Testing..."):
            try:
                session_service = InMemorySessionService()
                session = session_service.create_session(
                    app_name="test-app",
                    user_id=st.session_state.session_id
                )
                
                # Try different approaches
                st.write("**Method 1:** Direct agent.run()")
                result = weather_agent.run(
                    input_text=f"Weather in {location}",
                    session=session
                )
                st.write("Result:", result.output_text[:200] + "..." if len(result.output_text) > 200 else result.output_text)
                
                st.write("**Method 2:** Using Runner")
                try:
                    runner = Runner(agent=weather_agent, session=session)
                    runner_result = runner.run(input_text=f"Weather in {location}")
                    st.write("Runner result:", runner_result.output_text[:200] + "..." if len(runner_result.output_text) > 200 else runner_result.output_text)
                except Exception as e:
                    st.warning(f"Runner failed: {str(e)}")
                    
            except Exception as e:
                st.error(f"Error: {str(e)}")
                
except Exception as e:
    st.error(f"Import failed: {str(e)}")
