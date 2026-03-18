from question_generator import generate_questions
from data_store import save_candidate
from utils import validate_email, validate_phone, detect_sentiment

# English questions
questions_en = [
    "What is your Full Name?",
    "What is your Email Address?",
    "What is your Phone Number? (10 digits)",
    "How many years of experience do you have?",
    "What position are you applying for?",
    "What is your current location?",
    "Please list your tech stack (languages, frameworks, tools)"
]

# Hindi questions
questions_hi = [
    "आपका पूरा नाम क्या है?",
    "आपका ईमेल पता क्या है?",
    "आपका फोन नंबर क्या है? (10 अंक)",
    "आपके पास कितने वर्षों का अनुभव है?",
    "आप किस पद के लिए आवेदन कर रहे हैं?",
    "आपका वर्तमान स्थान क्या है?",
    "कृपया अपना टेक स्टैक बताएं (भाषाएं, फ्रेमवर्क, टूल्स)"
]


def process_input(user_input, state):

    # Exit
    if user_input.lower() in ["exit", "quit", "bye"]:
        return "धन्यवाद! हम आपसे संपर्क करेंगे।" if state.get("language") == "Hindi" else "Thank you for your time. TalentScout will contact you soon."

    language = state.get("language", "English")
    questions = questions_hi if language == "Hindi" else questions_en

    step = state.step

    # Sentiment detection
    sentiment = detect_sentiment(user_input)
    if sentiment == "negative":
        return "कोई बात नहीं, आप आराम से जवाब दें।" if language == "Hindi" else "I understand, take your time."

    # Validation
    if step == 1 and not validate_email(user_input):
        return "कृपया सही ईमेल दर्ज करें।" if language == "Hindi" else "Please enter a valid email address."

    if step == 2 and not validate_phone(user_input):
        return "कृपया सही 10 अंकों का फोन नंबर दर्ज करें।" if language == "Hindi" else "Please enter a valid 10-digit phone number."

    # Save data
    state.data[questions[step]] = user_input

    state.step += 1

    # Ask next question
    if state.step < len(questions):
        return questions[state.step]

    # Final step
    tech_stack = user_input
    tech_questions = generate_questions(tech_stack)

    save_candidate(state.data)

    name = state.data.get(questions[0], "Candidate")

    return f"""
{"धन्यवाद" if language == "Hindi" else "Thank you"} {name}.

{"आपकी जानकारी सफलतापूर्वक दर्ज की गई है।" if language == "Hindi" else "Your profile has been recorded successfully."}

{tech_questions}

{"हमारी टीम आपसे संपर्क करेगी।" if language == "Hindi" else "TalentScout recruitment team will contact you."}
"""