import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
   
   
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    
    if score == 4:
        feedback.append("✅ **Strong Password!**")
    elif score == 3:
        feedback.append("⚠️ **Moderate Password** - Consider adding more security features.")
    else:
        feedback.append("❌ **Weak Password** - Improve it using the suggestions above.")

    return feedback

st.title("🔐 Password Strength Checker")
st.title(" ")
st.subheader("Give me your password and i will tell you its strength")

password = st.text_input("Enter your password", type="password")

if password:
    results = check_password_strength(password)
    for line in results:
        st.write(line)
