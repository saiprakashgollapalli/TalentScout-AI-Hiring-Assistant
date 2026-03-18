import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
from prompts import TECH_QUESTION_PROMPT

# Load .env for local
load_dotenv()

# Get API key safely
api_key = None

try:
    # Try Streamlit Cloud secrets
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    # Fallback to local .env
    api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-pro")


def generate_questions(tech_stack):

    prompt = TECH_QUESTION_PROMPT.format(tech_stack=tech_stack)

    try:
        response = model.generate_content(prompt)

        if response.text:
            return f"""
### Technical Screening Questions

Based on your tech stack (**{tech_stack}**), here are some questions:

{response.text}
"""
        else:
            raise Exception("Empty response")

    except Exception:
        return f"""
### Technical Screening Questions

Based on your tech stack (**{tech_stack}**), here are sample questions:

Python
1. What are generators in Python?
2. Explain decorators in Python.

SQL
1. What is the difference between INNER JOIN and LEFT JOIN?
2. What are window functions?

Java
1. What is JVM and how does it work?
2. Explain JDK vs JRE vs JVM.

(Note: AI fallback used.)
"""