from question_generator import generate_questions
from data_store import save_candidate
from utils import validate_email, validate_phone, detect_sentiment

# =========================
# QUESTIONS (GLOBAL SCOPE)
# =========================

questions_en = [
    "What is your Full Name?",
    "What is your Email Address?",
    "What is your Phone Number? (10 digits)",
    "How many years of experience do you have?",
    "What position are you applying for?",
    "What is your current location?",
    "Please list your tech stack (languages, frameworks, tools)"
]

questions_hi = [
    "आपका पूरा नाम क्या है?",
    "आपका ईमेल पता क्या है?",
    "आपका फोन नंबर क्या है? (10 अंक)",
    "आपके पास कितने वर्षों का अनुभव है?",
    "आप किस पद के लिए आवेदन कर रहे हैं?",
    "आपका वर्तमान स्थान क्या है?",
    "कृपया अपना टेक स्टैक बताएं (भाषाएं, फ्रेमवर्क, टूल्स)"
]


# =========================
# MAIN FUNCTION
# =========================

def process_input(user_input, state):

    # Ensure state exists
    if "step" not in state:
        state.step = 0
    if "data" not in state:
        state.data = {}

    language = state.get("language", "English")
    questions = questions_hi if language == "Hindi" else questions_en

    # =========================
    # EXIT CONDITION
    # =========================
    if user_input.lower() in ["exit", "quit", "bye"]:
        return (
            "धन्यवाद! हम आपसे संपर्क करेंगे।"
            if language == "Hindi"
            else "Thank you for your time. TalentScout will contact you soon."
        )

    step = state.step

    # =========================
    # SENTIMENT DETECTION (BONUS)
    # =========================
    sentiment = detect_sentiment(user_input)
    if sentiment == "negative":
        return (
            "कोई बात नहीं, आप आराम से जवाब दें।"
            if language == "Hindi"
            else "I understand, take your time."
        )

    # =========================
    # VALIDATIONS
    # =========================
    if step == 1 and not validate_email(user_input):
        return (
            "कृपया सही ईमेल दर्ज करें।"
            if language == "Hindi"
            else "Please enter a valid email address."
        )

    if step == 2 and not validate_phone(user_input):
        return (
            "कृपया सही 10 अंकों का फोन नंबर दर्ज करें।"
            if language == "Hindi"
            else "Please enter a valid 10-digit phone number."
        )

    # =========================
    # STORE DATA
    # =========================
    state.data[questions[step]] = user_input

    # Move to next step
    state.step += 1

    # =========================
    # NEXT QUESTION
    # =========================
    if state.step < len(questions):
        return questions[state.step]

    # =========================
    # FINAL STEP → AI QUESTIONS
    # =========================
    tech_stack = user_input

    try:
        tech_questions = generate_questions(tech_stack)
    except Exception:
        tech_questions = "Unable to generate AI questions at the moment."

    save_candidate(state.data)

    name = state.data.get(questions[0], "Candidate")

    # Reset step to avoid bugs on reuse
    state.step = len(questions)

    return f"""
{"धन्यवाद" if language == "Hindi" else "Thank you"} {name}.

{"आपकी जानकारी सफलतापूर्वक दर्ज की गई है।" if language == "Hindi" else "Your profile has been recorded successfully."}

{tech_questions}

{"हमारी टीम आपसे संपर्क करेगी।" if language == "Hindi" else "TalentScout recruitment team will contact you."}
"""