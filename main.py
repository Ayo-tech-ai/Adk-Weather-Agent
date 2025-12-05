import streamlit as st
import uuid

st.set_page_config(page_title="Weather Agent", page_icon="⛅")
st.title("🌦️ Complete Weather Agent")

# Initialize
if 'setup_done' not in st.session_state:
    try:
        from google.adk.sessions import InMemorySessionService
        from google.adk.runners import Runner
        from agent.agent import weather_agent
        
        # Create services
        session_service = InMemorySessionService()
        
        # Create runner
        runner = Runner(
            agent=weather_agent,
            app_name="weather-agent-system",
            session_service=session_service
        )
        
        # Generate IDs
        user_id = str(uuid.uuid4())
        session_id = str(uuid.uuid4())
        
        # Store everything
        st.session_state.runner = runner
        st.session_state.user_id = user_id
        st.session_state.session_id = session_id
        st.session_state.session_service = session_service
        st.session_state.setup_done = True
        
        st.success("✅ System initialized!")
        
    except Exception as e:
        st.error(f"❌ Setup failed: {str(e)}")
        st.stop()

# Main interface
st.write("### Get Current Weather")
col1, col2 = st.columns([3, 1])
with col1:
    location = st.text_input("Enter location:", placeholder="City or place name")
with col2:
    if st.button("🔍 Search", use_container_width=True):
        pass  # Trigger below

if location and st.session_state.get('_trigger_search', False):
    with st.spinner(f"Getting weather for {location}..."):
        try:
            # Make the API call
            response = st.session_state.runner.run(
                user_id=st.session_state.user_id,
                session_id=st.session_state.session_id,
                new_message=f"Get current weather for {location}. Include temperature, conditions, humidity, wind speed, and any alerts."
            )
            
            # Display result
            st.success(f"✅ Weather for {location}")
            st.write(response.output_text)
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# Set trigger for next run
if st.button("🔍 Search", key="search_btn"):
    st.session_state._trigger_search = True
    st.rerun()
