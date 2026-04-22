import streamlit as st 
from time import sleep
st.title("Log in 🚪")
st.write("Please write your email and password")
with st.form("signin_form"):
    st.write("Your Email")
    email = st.text_input("E-mail")
    st.write("Your Password")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Sign In", use_container_width=True)
    if submit:
        if email and password:
            st.session_state['email'] = email
            st.session_state['password'] = password
            st.success("Logged in successfully! Welcome back.")
            sleep(3)
            st.switch_page("Pages/products.py")
        else:
            st.error("Please enter both email and password.")
st.divider()
st.write("Don't have an account?") 
st.write('Sign up now to enjoy our products!')
