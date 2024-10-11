import streamlit as st
import firebase_admin 
from firebase_admin import firestore

def app():
    # Initialize Firestore
    db = firestore.client()

    # Check if the user is logged in
    if 'username' in st.session_state and st.session_state.username != '':
        username = st.session_state.username
        st.title(f"Posts by {username}")

        # Retrieve user's posts from Firestore
        user_doc = db.collection("Posts").document(username).get()

        if user_doc.exists:
            posts = user_doc.to_dict().get('content', [])
            if posts:
                st.write("Your Posts:")
                for post in posts:
                    st.text_area(label="", value=post, height=100, disabled=True)  # Display each post as a read-only text area
            else:
                st.write("You have not posted anything yet.")
        else:
            st.write("No posts found for this user.")
    else:
        st.warning("Please log in to see your posts.")
