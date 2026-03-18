import streamlit as st
from chatbot_engine import process_input, questions

st.set_page_config(page_title="TalentScout Hiring Assistant")

# Sidebar
st.sidebar.title("TalentScout Hiring Assistant")

st.sidebar.markdown(
"""
Welcome to the **TalentScout AI Hiring Assistant**.

This assistant performs the **initial candidate screening process** by:

• Collecting candidate personal details  
• Understanding professional experience  
• Identifying the candidate's tech stack  
• Generating relevant technical interview questions  

You can type **exit** anytime in the chat to end the conversation.
"""
)

st.sidebar.markdown("---")

# Restart conversation button
if st.sidebar.button("Restart Conversation"):
    st.session_state.clear()
    st.rerun()

# Main title
st.title("🤖 TalentScout AI Hiring Assistant")

st.markdown(
"""
Welcome to **TalentScout Recruitment Agency**.

This AI assistant will guide you through a short screening process
by collecting your details and generating technical questions based
on your technology stack.
"""
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.step = 0
    st.session_state.data = {}

    # Greeting
    st.session_state.messages.append(
        ("assistant", "Hello! I am the TalentScout Hiring Assistant. Let's begin the screening process.")
    )

    # First question
    st.session_state.messages.append(
        ("assistant", questions[0])
    )

# Display chat history
for role, message in st.session_state.messages:

    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)

# User input
user_input = st.chat_input("Type your message here...")

if user_input:

    st.session_state.messages.append(("user", user_input))

    response = process_input(user_input, st.session_state)

    st.session_state.messages.append(("assistant", response))

    st.rerun()