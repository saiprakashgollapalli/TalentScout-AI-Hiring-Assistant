import streamlit as st
from chatbot_engine import process_input, questions_en, questions_hi

st.set_page_config(page_title="TalentScout Hiring Assistant", layout="wide")
progress = st.session_state.get("step", 0) / 7
st.progress(progress, text=f"Step {st.session_state.get('step', 0)+1} of 7")

# 🎨 ADVANCED UI STYLING
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}
.stChatMessage {
    border-radius: 12px;
    padding: 12px;
    margin-bottom: 10px;
}
[data-testid="stChatMessage-user"] {
    background-color: #1f77b4;
    color: white;
}
[data-testid="stChatMessage-assistant"] {
    background-color: #262730;
    color: white;
}
.stTextInput>div>div>input {
    border-radius: 20px;
}
</style>
""", unsafe_allow_html=True)

# 🌍 Language selector
language = st.sidebar.selectbox("🌍 Select Language", ["English", "Hindi"])
st.session_state.language = language

# Sidebar
st.sidebar.title("🎯 TalentScout Assistant")
st.sidebar.info("AI-powered candidate screening chatbot")


if st.sidebar.button("🔄 Restart"):
    st.session_state.clear()
    st.rerun()

# Main Title
st.markdown("""
<h1 style='text-align: center; color: white;'>
🤖 TalentScout AI Hiring Assistant
</h1>
""", unsafe_allow_html=True)

st.success("🚀 AI-powered Hiring Assistant is ready!")

# Select questions
questions = questions_hi if language == "Hindi" else questions_en

# Initialize session
if "step" not in st.session_state or st.session_state.get("language") != language:
    st.session_state.step = 0
    st.session_state.data = {}
    st.session_state.messages = []
    st.session_state.language = language

    questions = questions_hi if language == "Hindi" else questions_en

    greeting = (
        "नमस्ते! मैं TalentScout Hiring Assistant हूँ।"
        if language == "Hindi"
        else "Hello! I am the TalentScout Hiring Assistant."
    )

    st.session_state.messages.append(("assistant", greeting))
    st.session_state.messages.append(("assistant", questions[0]))
# 💬 Display chat with avatars
for role, message in st.session_state.messages:
    if role == "assistant":
        with st.chat_message("assistant", avatar="🤖"):
            st.markdown(message)
    else:
        with st.chat_message("user", avatar="👤"):
            st.markdown(message)

# 💬 Input box
user_input = st.chat_input("💬 Type your message...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    with st.spinner("🤖 Thinking..."):
        response = process_input(user_input, st.session_state)

    st.session_state.messages.append(("assistant", response))

    st.rerun()
    st.markdown("""
<style>
[data-testid="stChatMessage-user"] {
    text-align: right;
}
[data-testid="stChatMessage-assistant"] {
    text-align: left;
}
</style>
""", unsafe_allow_html=True)