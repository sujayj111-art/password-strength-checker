import streamlit as st
import re

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter Password", type="password")

if st.button("Check Password"):

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
        st.error("Weak Password")
    elif score <= 4:
        st.warning("Medium Password")
    else:
        st.success("Strong Password")