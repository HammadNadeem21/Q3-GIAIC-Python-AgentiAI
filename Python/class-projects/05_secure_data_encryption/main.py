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