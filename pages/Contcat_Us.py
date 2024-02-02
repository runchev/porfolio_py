import streamlit as st
import send_email as mail_sender
st.header("Contact me")

with st.form("email_form"):
    st.text_input("Your email", key="email", placeholder="Enter your email here...")
    st.text_area("Your message", key="message", placeholder="Enter your message here")
    submit = st.form_submit_button("Send")
    if submit:
        session = st.session_state
        mail_sender.send_email(session['email'], session['message'])
        st.info("Your mail was sent successfully")
