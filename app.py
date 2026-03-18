import streamlit as st
from chatbot_engine import process_input, questions

st.set_page_config(page_title="TalentScout Hiring Assistant")

# Sidebar
st.sidebar.title("TalentScout Hiring Assistant")

st.sidebar.markdown(
"""
Welcome to the **TalentScout AI Hiring Assistant**.

This assistant performs the **initial candidate screening process**.

Type **exit** anytime to end the conversation.
"""
)

st.sidebar.markdown("---")

# Restart button
if st.sidebar.button("Restart Conversation"):
    st.session_state.clear()
    st.rerun()

# Title
st.title("🤖 TalentScout AI Hiring Assistant")

st.markdown(
"""
Welcome to **TalentScout Recruitment Agency**.

Let's begin your screening process.
"""
)

# Initialize state ONLY ONCE
if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.messages = []

    # Greeting + first question
    st.session_state.messages.append(
        ("assistant", "Hello! I am the TalentScout Hiring Assistant. Let's begin the screening process.")
    )
    st.session_state.messages.append(
        ("assistant", questions[0])
    )

# Display chat
for role, message in st.session_state.messages:
    st.chat_message(role).write(message)

# Input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append(("user", user_input))

    response = process_input(user_input, st.session_state)

    st.session_state.messages.append(("assistant", response))

    st.rerun()