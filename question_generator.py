import google.generativeai as genai
import streamlit as st
from prompts import TECH_QUESTION_PROMPT

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-pro")


def generate_questions(tech_stack):

    prompt = TECH_QUESTION_PROMPT.format(tech_stack=tech_stack)

    try:
        response = model.generate_content(prompt)

        return f"""
### Technical Screening Questions

Based on your tech stack (**{tech_stack}**), here are some questions:

{response.text}
"""

    except Exception:
        return "Error generating questions. Please try again."