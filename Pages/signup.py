import streamlit as st 
from time import sleep

st.title("Create Account 📝")
st.write("Join our team today!")
with st.form("signup_form"):
    st.write("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name", value="Amira Hassan")
        email = st.text_input("Email", value="example@gmail.com")
    with col2:
        phone = st.text_input("Phone Number", value="+1234567890")
        password = st.text_input("Password", type="password")
    st.write("Delivery Information")
    col3, col4 = st.columns([0.7,0.3])
    with col3:
         address = st.text_input("Street address", value="123 Main St, City, Country")
    with col4:
        apartment_number = st.number_input("Apartment number", value=1, min_value=1 )
    submit = st.form_submit_button('Create Account',use_container_width=True)
    if submit:
        if name and email and phone and password and address:
            st.session_state['name'] = name
            st.session_state['phone'] = phone
            st.session_state['email'] = email
            st.session_state['address'] = address
            st.session_state['apartment_number'] = apartment_number
            st.success("Account created successfully! Please sign in to order")
            sleep (3)
            st.switch_page("Pages/signin.py")
        else:
                st.error("Please fill in all the required fields.")
st.divider()
st.write("Already have an account?")
if st.button("Sign In Here", use_container_width=True):
    sleep (2)
    st.switch_page("Pages/signin.py")
