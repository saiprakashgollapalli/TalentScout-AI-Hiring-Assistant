# TalentScout AI Hiring Assistant

## Overview
TalentScout AI Hiring Assistant is an intelligent chatbot designed to automate the initial candidate screening process for technology roles.

The system collects candidate details and dynamically generates technical interview questions based on the candidate’s declared tech stack using Large Language Models (LLMs).

---

## Features
- Candidate information collection (Name, Email, Phone, Experience, Role, Location)
- Tech stack-based dynamic question generation
- Context-aware conversation flow
- Input validation (Email & Phone)
- Fallback mechanism for AI failures
- Streamlit-based interactive UI
- Restart conversation feature

---

## Tech Stack
- Python
- Streamlit
- Google Gemini API
- Prompt Engineering

---

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py
