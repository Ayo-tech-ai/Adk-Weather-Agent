import streamlit as st

st.set_page_config(page_title="Weather Agent Debug", page_icon="🐛")
st.title("🔍 Runner.run() Debug")

try:
    from google.adk.sessions import InMemorySessionService
    from google.adk.runners import Runner
    from agent.agent import weather_agent
    import inspect
    
    # Setup
    session_service = InMemorySessionService()
    runner = Runner(
        agent=weather_agent,
        app_name="debug_app",
        session_service=session_service
    )
    
    # Check run() method signature
    st.write("### Runner.run() Parameters")
    sig = inspect.signature(runner.run)
    params = list(sig.parameters.keys())
    st.write(f"runner.run accepts: {params}")
    
    st.write("### Test Different Calling Patterns")
    location = "Lagos"
    
    # Test 1: Positional argument
    st.write("**Test 1:** Positional argument")
    try:
        response1 = runner.run(f"Weather in {location}")
        st.success(f"✅ Works! Response: {response1.output_text[:100]}...")
    except Exception as e1:
        st.error(f"❌ Failed: {str(e1)}")
    
    # Test 2: With session parameter
    st.write("**Test 2:** With session parameter")
    try:
        session = session_service.create_session(
            app_name="test_session",
            user_id="test_user_123"
        )
        response2 = runner.run(f"Weather in {location}", session=session)
        st.success(f"✅ Works! Response: {response2.output_text[:100]}...")
    except Exception as e2:
        st.error(f"❌ Failed: {str(e2)}")
    
    # Test 3: Check response object
    st.write("**Test 3:** Response Object Structure")
    try:
        response3 = runner.run("Weather in Tokyo")
        st.write("Response type:", type(response3))
        st.write("Response attributes:", dir(response3))
        if hasattr(response3, 'output_text'):
            st.write("output_text:", response3.output_text[:200])
    except Exception as e3:
        st.error(f"Test 3 failed: {str(e3)}")
        
except Exception as e:
    st.error(f"Debug setup failed: {str(e)}")
