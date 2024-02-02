import streamlit as st

st.header("Contact me")

with st.form("email_form"):
    st.text_input("Your email", key="email", placeholder="Enter your email here...")
    st.text_area("Your message", key="message", placeholder="Enter your message here")
    submit = st.form_submit_button("Send")

    if submit:
        print("ok")