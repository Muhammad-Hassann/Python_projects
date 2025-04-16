import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Initialize session state variables
if "KEY" not in st.session_state:
    st.session_state.KEY = Fernet.generate_key()
    st.session_state.cipher = Fernet(st.session_state.KEY)
if "stored_data" not in st.session_state:
    st.session_state.stored_data = {}
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "menu" not in st.session_state:
    st.session_state.menu = "Home"  # Default menu option

# Hashing function
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt data
def encrypt_data(data):
    return st.session_state.cipher.encrypt(data.encode()).decode()

# Decrypt data
def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)
    for key, value in st.session_state.stored_data.items():
        if key == encrypted_text and value["passkey"] == hashed_passkey:
            try:
                decrypted_data = st.session_state.cipher.decrypt(encrypted_text.encode()).decode()
                return decrypted_data
            except:
                st.session_state.failed_attempts += 1
                return None
    st.session_state.failed_attempts += 1
    return None

# Streamlit UI
st.title("🔐 Secure Data Encryption App")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Menu", menu, index=menu.index(st.session_state.menu))

if choice == "Home":
    st.subheader("Welcome!")
    st.write("Use this app to securely **store and retrieve encrypted data**.")
    st.write("Choose an option from the menu.")

elif choice == "Store Data":
    st.subheader("🔏 Store Data Securely")
    data = st.text_area("Enter the data to be stored:")
    passkey = st.text_input("Enter a passkey for the data:", type="password")

    if st.button("Encrypt and Save"):
        if data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(data)
            st.session_state.stored_data[encrypted_text] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            st.success("✅ Data encrypted and stored successfully!")
            st.code(encrypted_text, language="text")
        else:
            st.error("❗ Please enter both data and passkey.")

elif choice == "Retrieve Data":
    st.subheader("🔓 Retrieve Data Securely")
    encrypted_text = st.text_input("Enter the encrypted text:")
    passkey = st.text_input("Enter the passkey:", type="password")

    if st.button("Decrypt and Retrieve"):
        if encrypted_text and passkey:
            decrypted_data = decrypt_data(encrypted_text, passkey)
            if decrypted_data:
                st.success(f"✅ Decrypted Data: {decrypted_data}")
                st.session_state.failed_attempts = 0  # reset attempts after success
            else:
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("🚫 Too many failed attempts! Redirecting to Login Page.")
                    st.session_state.failed_attempts = 0  # reset attempts
                    st.session_state.menu = "Login"  # switch to login menu
                    st.rerun()  # rerun to update UI
        else:
            st.error("❗ Please enter both the encrypted text and the passkey.")

elif choice == "Login":
    st.subheader("🔐 Login")
    username = st.text_input("Enter your username:")
    password = st.text_input("Enter your password:", type="password")

    if st.button("Login"):
        if username == "admin" and password == "admin":
            st.success("✅ Logged in successfully!")
            st.write("Welcome, admin! You now have access to all features.")
            st.session_state.menu = "Home"  # Go back to Home after login
            st.rerun()  # rerun to switch back to Home page
        else:
            st.error("❌ Invalid username or password.")
