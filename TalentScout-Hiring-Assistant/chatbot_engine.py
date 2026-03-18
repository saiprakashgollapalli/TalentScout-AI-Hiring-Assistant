from question_generator import generate_questions
from data_store import save_candidate
from utils import validate_email, validate_phone

questions = [
    "What is your Full Name?",
    "What is your Email Address?",
    "What is your Phone Number? (10 digits)",
    "How many years of experience do you have?",
    "What position are you applying for?",
    "What is your current location?",
    "Please list your tech stack (languages, frameworks, tools)"
]

candidate_data = {}

current_step = 0


def process_input(user_input):

    global current_step

    if user_input.lower() in ["exit", "quit", "bye"]:
        return "Thank you for your time. TalentScout will contact you soon."

    # Email validation
    if current_step == 1:
        if not validate_email(user_input):
            return "Please enter a valid email address."

    # Phone validation
    if current_step == 2:
        if not validate_phone(user_input):
            return "Please enter a valid 10-digit phone number."

    if current_step < len(questions):

        key = questions[current_step]

        candidate_data[key] = user_input

        current_step += 1

        if current_step < len(questions):

            return questions[current_step]

        else:

            tech_stack = user_input

            tech_questions = generate_questions(tech_stack)

            save_candidate(candidate_data)

            return f"""
Thank you for providing your details.

Your profile has been recorded successfully.

{tech_questions}

TalentScout recruitment team will review your profile and contact you for the next steps.
"""

    return "Thank you!"