import streamlit as st
import uuid

st.set_page_config(page_title="Weather Agent", page_icon="⛅")
st.title("🌦️ Weather Agent with History")

# Initialize session state
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if 'conversation' not in st.session_state:
    st.session_state.conversation = []
if 'runner' not in st.session_state:
    # Initialize runner once
    try:
        from google.adk.sessions import InMemorySessionService
        from google.adk.runners import Runner
        from agent.agent import weather_agent
        
        session_service = InMemorySessionService()
        session = session_service.create_session(
            app_name="weather-chat",
            user_id=st.session_state.session_id
        )
        
        st.session_state.runner = Runner(
            agent=weather_agent,
            session=session
        )
        st.success("✅ Agent initialized")
    except Exception as e:
        st.error(f"Failed to initialize agent: {str(e)}")

# Display conversation history
for msg in st.session_state.conversation:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input for new location
if prompt := st.chat_input("Enter a location for weather info:"):
    # Add user message to history
    st.session_state.conversation.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)
    
    # Get weather response
    with st.chat_message("assistant"):
        with st.spinner("Searching..."):
            try:
                response = st.session_state.runner.run(
                    input_text=f"Get current weather for {prompt}"
                )
                
                # Display response
                st.write(response.output_text)
                
                # Add to conversation history
                st.session_state.conversation.append({
                    "role": "assistant", 
                    "content": response.output_text
                })
                
            except Exception as e:
                error_msg = f"Error: {str(e)}"
                st.error(error_msg)
                st.session_state.conversation.append({
                    "role": "assistant", 
                    "content": error_msg
                })
