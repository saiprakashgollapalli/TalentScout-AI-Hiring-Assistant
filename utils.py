import re

def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10



def detect_sentiment(text):
    negative_words = ["bad", "hard", "difficult", "confusing"]

    words = re.findall(r'\b\w+\b', text.lower())

    for word in negative_words:
        if word in words:
            return "negative"

    return "neutral"