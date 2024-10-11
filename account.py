import streamlit as st
import firebase_admin 
from firebase_admin import credentials, auth
import json

# Accessing credentials from secrets
client_email = st.secrets["credentials"]["client_email"]
private_key = st.secrets["credentials"]["private_key"]

# Initialize Firebase Admin with the credentials
import firebase_admin
from firebase_admin import credentials

# Convert private_key to a format that Firebase expects
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "methiong",
    "private_key_id": "6db79f6eb23d2252392603c6f8c7459061ea84c9",
    "private_key": private_key,
    "client_email": client_email,
    "client_id": "101174810610348602334",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-9c1d2%40methiong.iam.gserviceaccount.com"
})

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)


def app():
    st.title("It's An :red[Account Page] :moon:")
    
    if 'username' not in st.session_state:
        st.session_state.username=''
    if 'useremail' not in st.session_state:
        st.session_state.useremail=''
    def f():
        try:
            user=auth.get_user_by_email(email)
            
            st.write("YO in")

            st.session_state.username=user.uid
            st.session_state.useremail=user.email

            st.session_state.signout=True
            st.session_state.signedout=True

        except:
            st.warning("Login failed")

    def t():
        st.session_state.signout=False
        st.session_state.signedout=False

    if 'signedout' not in st.session_state:
        st.session_state.signedout=False
    if 'signout' not in st.session_state:
        st.session_state.signout=False

    if not st.session_state['signedout']:
        choice=st.selectbox("Login/signup",['Login',"Signup"])

        if choice =="Login":
            email=st.text_input("email")
            password=st.text_input("password",type='password')

            st.button("Login",on_click=f)
        else:
            Username=st.text_input('Username')
            email=st.text_input("email")
            password=st.text_input("password",type='password')

            if st.button("signup:smile:"):
                st.write("hurray")
                user=auth.create_user(email=email,password=password,uid=Username)

                st.success("Account created successfully")
                st.markdown("""
                            # Please login using your email and password
                            """)
                st.balloons()
    if st.session_state.signout:
        st.markdown("""# Hello """+st.session_state.username)
        st.button("signout",on_click=t)



