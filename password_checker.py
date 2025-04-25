import string
import random
import re

def evaluate_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Use a mix of uppercase and lowercase letters.")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    common_words = ['password', '123456', 'qwerty', 'admin', 'letmein']
    if any(word in password.lower() for word in common_words):
        feedback.append("Avoid using common or predictable words.")
    else:
        score += 1

    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, feedback

def generate_random_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_strong_from_input(user_input):
    base = user_input.capitalize()  # Capitalize first letter
    digits = ''.join(random.choices(string.digits, k=4))
    specials = ''.join(random.choices('@#$%&*!?', k=2))
    return specials + base + digits

def suggest_passwords(user_input):
    suggestions = [
        generate_strong_from_input(user_input),
        generate_random_password(),
        generate_random_password()
    ]
    return suggestions

def main():
    password = input("Enter your password to check: ")
    strength, suggestions = evaluate_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if suggestions:
        print("Suggestions:")
        for tip in suggestions:
            print(f"- {tip}")

    print("\nSuggested Strong Passwords:")
    for pwd in suggest_passwords(password):
        print(f"- {pwd}")

if __name__ == "__main__":
    main()
