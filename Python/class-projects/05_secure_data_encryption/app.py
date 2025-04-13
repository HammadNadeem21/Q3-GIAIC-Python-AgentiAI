import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac


# Collect Data Information 
data_file = "secure_data.json"
salt = b"secure_salt_value"
lockout_duration = 60


if "authentic_user" not in st.session_state:
    st.session_state.authentic_user = None

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0


if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0



# data load
def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return {}



# data write
def save_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f)



# Generate Key
def generate_key(passkey):
    key = pbkdf2_hmac('sha256', passkey.encode(), salt, 100000)
    return urlsafe_b64encode(key)


def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000).hex()



def encrypt_text(text, key):
    cipher = Fernet(generate_key(key))
    return cipher.encrypt(text.encode()).decode()

def decrypt_text(encrypt_text, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypt_text.encode()).decode()
    except:
        return None
    

stored_data = load_data()


# Navigation
st.title("🛡️ Secure Data Encryption System")
menu = ["Home", "Register", "Login", "Store Data", "Retrieve Data"]
choice = st.sidebar.selectbox("Navigation", menu)


# Home Page
if choice == "Home":
    st.subheader(" Welcome to my Data Encryption System")
    st.markdown("Develop a Streamlit-based secure data storage and retrieval system where:\nUsers store data with a unique passkey.\nUsers decrypt data by providing the correct passkey.\nMultiple failed attempts result in a forced reauthorization (login page).\nThe system operates entirely in memory without external databases.")

# user registration
elif choice == "Register":
    st.subheader("📝 Register New User")
    username = st.text_input("Choose Username")
    password = st.text_input("Choose Password", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.warning("⚠️ User already exisits.")
            else:
                stored_data[username] = {
                    "password":hash_password(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("✅ User register sucess")
        else:
            st.error("Boh feilds are required.")
    
elif choice == "Login":
        st.subheader("🔑 User Login")

        if time.time() < st.session_state.lockout_time:
            remaining = int(st.session_state.lockout_time - time.time())
            st.error(f"⏳ Too many failed attempts. Please wait {remaining} seconds.")
            st.stop()

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")


        if st.button("Login"):
            if username in stored_data and stored_data[username]["password"] == hash_password(password):
                st.session_state.authentic_user = username
                st.session_state.failed_attempts = 0
                st.success(f"😀 Welcome {username}")

            else:
                st.session_state.failed_attempts += 1
                remaining = 3 - st.session_state.failed_attempts
                st.error(f"❌ Invalid Credentials! Attempts left: {remaining}")

                if st.session_state.failed_attempts >= 3:
                    st.session_state.lockout_time = time.time() + lockout_duration
                    st.error(f"🚫 Too many failed attempts. Locked for 60 seconds.")
                    st.stop()



# Data Store Section

elif choice == "Store Data":
    if not st.session_state.authentic_user:
        st.warning("Please login first")
    else:
        st.subheader("📁 Store Encrypted Data")
        data = st.text_area("Enter data to encrypt")
        passkey = st.text_input("Encryption key (passphrase)", type="password")

        if st.button("Encrypt and save"):
            if data and passkey:
                encrypted = encrypt_text(data, passkey)
                stored_data[st.session_state.authentic_user]["data"].append(encrypted)
                save_data(stored_data)
                st.success("✅ Data encrypted and save sucessfuly!")

            else:
                st.error("All fields are required to fill.")


# data retieve section
elif choice == "Retrieve Data":
    if not st.session_state.authentic_user:
        st.warning("Please login first")
    else:
        st.subheader("🔍 Retrieve Data")
        user_data = stored_data.get(st.session_state.authentic_user, {}).get("data", [])

        if not user_data:
            st.info("No Data found!")
        else:
            st.write("Encrypted Data Entries:")
            for i, item in enumerate(user_data):
                st.code(item, language="text")

            encrypted_input = st.text_area("Enter Encrypted Text")
            passkey = st.text_input("Enter Passkey To Decrypt", type="password")

            if st.button("Decrypt"):
                result = decrypt_text(encrypted_input, passkey)
                if result:
                    st.success(f"✅ Decrypted : {result}")
                else:
                    st.error("❌ Incorrect passkey or corrupted data.")