import streamlit as st
import firebase_admin 
from firebase_admin import firestore

def app():
    if 'db' not in st.session_state:
        st.session_state.db=''
    db=firestore.client()
    st.session_state.db=db

    ph=''
    if st.session_state.username=='':
        ph="Login to be able to post"
    else:
        ph='Post your thoughts'

    post=st.text_area(label=" :green[ +New post buddy]",placeholder=ph,max_chars=1000) 
    if st.button("post",use_container_width=50):
        if post!='' and 'username' in st.session_state:
            doc_ref=db.collection("Posts").document(st.session_state.username)
            info=doc_ref.get()
            if info.exists and 'content' in info.to_dict():
                pos=db.collection("Posts").document(st.session_state.username)
                pos.update({u'content':firestore.ArrayUnion([u'{}'.format(post)])})
                st.markdown("""# :green[POST Uploaded] :white_check_mark:""")
            else:
                data={'content':[post],'username':st.session_state.username}
                db.collection('Posts').document(st.session_state.username).set(data)
        else:
            data={'content':[post],'username':st.session_state.username}
            db.collection('Posts').document(st.session_state.username).set(data)
    docs=db.collection('Posts').get()

    for doc in docs:
        d=doc.to_dict()
        print(doc)
        print("Documents:",d)
        try:
            username=d.get('username','Unknown')
            content=d.get('content',[])
            if content:
                st.text_area(label=":green[Posted by:]"+" :orange[ {un} ]".format(un=d['username']),value=d['content'][-1],height=50,disabled=True)
            
        except Exception as e:
            st.write(f'error displaying post:{e}')