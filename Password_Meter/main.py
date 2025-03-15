import re
import streamlit as st
import random
import string

def check_password_strength(password):
    score = 0
    common_passwords = ["password", "123456", "qwerty", "admin", "letmein", "welcome", "123", "abc", "password1", "password123", "123456789", "12345678", "1234567890", "password!", "password123!", "qwerty123", "admin123", "letmein123", "welcome123", "abc123", "password1!", "password123!", "qwerty123!", "admin123!", "letmein123!", "welcome123!", "abc123!"]
    suggestions = []
    result = ''
    
    # Length Check
    if password in common_passwords:
        suggestions.append("❌ Avoid using common passwords.")
        result = "Weak"
        return score, suggestions, result
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(f"[{re.escape(string.punctuation)}]", password):
        score += 1
    else:
        suggestions.append("❌ Include at least one special character (!@#$%^&*).")
    
    return score, suggestions, result

def get_strong_password(length = 10):
    characters = string.ascii_letters + string.digits + string.punctuation
    for _ in range(10):
        password = ''.join(random.choice(characters) for _ in range(length))
    return password
    

# GUI with streamlit
# Strength Checker
st.set_page_config(page_title= "Password Strength Checker", page_icon= "🔑")
st.title("Password Strength Checker")

password_input = st.text_input("Enter your password:", type="password")

if st.button("Check Password"):
    if password_input:
        score, suggestions, result = check_password_strength(password_input)
        st.write("**Password Lenght:**", str(len(password_input)))
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")

        for suggestion in suggestions:
                st.write(suggestion)    


# Strong Password Generator
st.markdown("---")
st.title("Strong Password Generator")
password_len = st.slider("Choose password length:", value=10, min_value=8, max_value=24)

if st.button("Generate Password"):
    strong_password = get_strong_password(password_len)
    st.write("Generated Password:")
    st.code(strong_password)