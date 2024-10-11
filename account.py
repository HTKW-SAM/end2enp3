import streamlit as st
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import auth
import os
from dotenv import load_dotenv

load_dotenv()
firebase_credentials = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
print(firebase_credentials)
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_credentials)
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



