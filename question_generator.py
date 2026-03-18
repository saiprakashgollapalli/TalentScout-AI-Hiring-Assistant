import google.generativeai as genai
import streamlit as st
import os
from dotenv import load_dotenv
from prompts import TECH_QUESTION_PROMPT

# Load local env
load_dotenv()

# Safe API key loading
def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]  # Cloud
    except Exception:
        return os.getenv("GEMINI_API_KEY")  # Local

api_key = get_api_key()

if not api_key:
    raise ValueError("API key not found. Check .env or Streamlit secrets.")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-pro")


def generate_questions(tech_stack):

    prompt = TECH_QUESTION_PROMPT.format(tech_stack=tech_stack)

    try:
        response = model.generate_content(prompt)

        if response and response.text:
            return f"""
### Technical Screening Questions

Based on your tech stack (**{tech_stack}**), here are some questions:

{response.text}
"""
        else:
            raise Exception("Empty response")

    except Exception as e:
        return f"""
### Technical Screening Questions

Based on your tech stack (**{tech_stack}**), here are sample questions:

Python
1. What are generators in Python?
2. Explain decorators in Python.

SQL
1. Difference between INNER JOIN and LEFT JOIN?
2. What are window functions?

Java
1. What is JVM?
2. Explain JDK vs JRE vs JVM.

(Note: AI fallback used due to API issue.)
"""