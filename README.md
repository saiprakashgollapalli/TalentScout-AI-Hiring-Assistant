# TalentScout AI Hiring Assistant

## 1. Project Overview

The TalentScout AI Hiring Assistant is an intelligent chatbot designed to automate the initial screening process for candidates applying to technology roles.

The system interacts with candidates in a conversational manner, collects essential details, and generates technical interview questions based on the candidate’s declared tech stack using Large Language Models (LLMs).

This project demonstrates the practical application of AI in recruitment workflows, improving efficiency and scalability in candidate screening.

---

## 2. Objectives

* Automate initial candidate screening
* Collect structured candidate information
* Generate relevant technical questions dynamically
* Maintain a smooth and context-aware conversation flow
* Ensure robustness with validation and fallback mechanisms

---

## 3. Features

### 3.1 Candidate Information Collection

The chatbot collects:

* Full Name
* Email Address
* Phone Number
* Years of Experience
* Desired Position
* Current Location
* Tech Stack

---

### 3.2 Tech Stack-Based Question Generation

* Dynamically generates 3–5 technical questions
* Tailored to technologies like Python, SQL, Java, etc.
* Uses prompt engineering with LLM

---

### 3.3 Context-Aware Conversation

* Maintains conversation flow using `st.session_state`
* Ensures structured step-by-step interaction

---

### 3.4 Input Validation

* Email format validation
* Phone number validation (10 digits)

---

### 3.5 Fallback Mechanism

* If AI fails → predefined questions are shown
* Ensures uninterrupted user experience

---

### 3.6 User Interface

* Built using Streamlit
* Clean and interactive chat-based UI
* Restart conversation feature

---

## 4. Tech Stack

| Category      | Technology               |
| ------------- | ------------------------ |
| Language      | Python                   |
| Frontend      | Streamlit                |
| AI Model      | Google Gemini (LLM)      |
| Backend Logic | Python modules           |
| Data Storage  | JSON (simulated storage) |

---

## 5. System Architecture

* **app.py** → Streamlit UI
* **chatbot_engine.py** → Conversation flow logic
* **question_generator.py** → LLM interaction
* **utils.py** → Input validation
* **data_store.py** → Candidate data storage
* **prompts.py** → Prompt templates

---

## 6. Prompt Engineering Strategy

Prompts were designed to:

* Guide the model to generate **relevant technical questions**
* Ensure questions match the **candidate's tech stack**
* Maintain a **professional and interview-like tone**
* Handle diverse technologies dynamically

Example:
If user enters:

> Python, SQL

The system generates:

* Python-based coding and concept questions
* SQL query and database-related questions

---

## 7. Data Handling & Privacy

* Uses simulated/local JSON storage (`candidates.json`)
* Sensitive data (API keys) stored securely using:

  * `.env` (local)
  * `Streamlit Secrets` (cloud)
* No real personal data is exposed publicly

---

## 8. Challenges & Solutions

### Challenge 1: Conversation State Reset

* **Problem:** Streamlit reruns script on each input
* **Solution:** Used `st.session_state` to persist data

---

### Challenge 2: API Key Handling (Local vs Cloud)

* **Problem:** Secrets not available locally
* **Solution:** Hybrid approach using `.env` + `st.secrets`

---

### Challenge 3: AI Failures

* **Problem:** API errors or empty responses
* **Solution:** Implemented fallback question system

---

### Challenge 4: Deployment Issues

* **Problem:** Nested folder structure broke deployment
* **Solution:** Cleaned project structure and redeployed

---

## 9. Deployment

* Platform: Streamlit Cloud
* Features:

  * Live chatbot interaction
  * Secure API key handling
  * Real-time AI question generation

---

## 10. How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 11. Future Enhancements

* Sentiment analysis during interaction
* Multi-language support
* Candidate scoring system
* Integration with real databases
* Resume parsing feature

---

## 12. Conclusion

The TalentScout AI Hiring Assistant successfully demonstrates how AI and LLMs can be used to streamline recruitment processes.

It provides a scalable, efficient, and intelligent solution for initial candidate screening while ensuring a smooth user experience through robust design and prompt engineering.

---

