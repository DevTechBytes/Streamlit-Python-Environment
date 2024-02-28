import streamlit as st

# configures page settings
st.set_page_config(
    page_title="Streamlit Demo",
    initial_sidebar_state="expanded"
)

# page title
st.title("Streamlit Demo")

with st.sidebar:
    st.number_input("Set Model Temperature", 0.1, 1.0, 0.7)
    st.slider("Max Token Length", 50, 500, 250)
    st.number_input("Set Top P", 0.1, 0.99, 0.99)

if user_prompt := st.chat_input("What would you like to ask?"):
    pass

with st.chat_message("user"):
    st.markdown("Who are you?")

with st.chat_message("assistant"):
    st.markdown("I am a helpinful assistant")

