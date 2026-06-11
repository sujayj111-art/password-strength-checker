import re

def check_password_strength(password):
    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1

    # Number Check
    if re.search(r"\d", password):
        score += 1

    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    # Strength Rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength


password = input("Enter Password: ")

score, strength = check_password_strength(password)

print("\nPassword Analysis")
print("------------------")
print("Score:", score, "/5")
print("Strength:", strength)