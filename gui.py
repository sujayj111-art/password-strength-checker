import tkinter as tk
import re

# Password Strength Function
def check_password():
    password = entry.get()

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        result = "Weak Password"
    elif score <= 4:
        result = "Medium Password"
    else:
        result = "Strong Password"

    result_label.config(text=result)

# Main Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

# Heading
title = tk.Label(root, text="Password Strength Checker", font=("Arial", 16))
title.pack(pady=10)

# Password Input
entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=10)

# Check Button
check_btn = tk.Button(root, text="Check Password", command=check_password)
check_btn.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()

root.mainloop()
