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


def process_input(user_input, state):

    # Exit
    if user_input.lower() in ["exit", "quit", "bye"]:
        return "Thank you for your time. TalentScout will contact you soon."

    step = state.step

    # Validation
    if step == 1 and not validate_email(user_input):
        return "Please enter a valid email address."

    if step == 2 and not validate_phone(user_input):
        return "Please enter a valid 10-digit phone number."

    # Save data
    state.data[questions[step]] = user_input

    # Move step forward
    state.step += 1

    # Ask next question
    if state.step < len(questions):
        return questions[state.step]

    # Final step
    tech_stack = user_input

    tech_questions = generate_questions(tech_stack)

    save_candidate(state.data)

    # Reset step to avoid bugs after completion
    state.step = len(questions)

    return f"""
Thank you for providing your details.

Your profile has been recorded successfully.

{tech_questions}

TalentScout recruitment team will review your profile and contact you for the next steps.
"""