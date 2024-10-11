import streamlit as st 
from streamlit_option_menu import option_menu

import about,account,home,trending,your_post

st.set_page_config(page_title='My_first_app')

class Multiapp:

    def __init__(self):
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({
            'title':title,
            "function":function
        })
    def run():
        with st.sidebar:
            app=option_menu(
                menu_title="ability",
                options=['home','account','trending','your_post','about'],
                icons=['house-fill','person-circle','trophy-fill'],
                menu_icon="chat-text-fill",
                default_index=1,
                styles={}
            )
        if app=='home':
            home.app()
        if app=='account':
            account.app()
        if app=='trending':
            trending.app()
        if app=='your_post':
            your_post.app()
        if app=='about':
            about.app()
Multiapp.run()