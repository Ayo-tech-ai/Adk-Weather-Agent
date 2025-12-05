import streamlit as st
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
            response = weather_agent.run(
                prompt=f"Get the current weather for {location}."
            )

        st.subheader("Weather Result")
        st.write(response.text)
