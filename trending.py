import streamlit as st
import firebase_admin 
from firebase_admin import firestore

def app():
    # Initialize Firestore
    db = firestore.client()

    st.title("Trending Posts")

    # Retrieve all posts from Firestore
    posts_ref = db.collection("Posts")
    all_posts = posts_ref.get()

    if all_posts:
        trending_posts = []
        for post_doc in all_posts:
            post_data = post_doc.to_dict()
            username = post_data.get('username', 'Unknown')
            content = post_data.get('content', [])

            if content:
                # Assuming the last entry in the content list is the most recent post
                trending_posts.append((username, content[-1]))

        # Sort posts by some criteria (e.g., by content length or any custom logic)
        trending_posts.sort(key=lambda x: len(x[1]), reverse=True)  # Example: sort by content length

        # Display trending posts
        st.write("Here are some trending posts:")
        for username, content in trending_posts:
            st.text_area(label=f"Posted by: {username}", value=content, height=100, disabled=True)
    else:
        st.write("No trending posts available at the moment.")
