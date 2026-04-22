import streamlit as st
home_page = st.Page(
    page='Pages/home.py',
    title="home page",
    icon='🏠' ,
    default=True
)
products_page=st.Page(
    page='Pages/products.py',
    title='our products',
    icon='📕'
)
sign_in = st.Page(
    page='Pages/signin.py' ,
    title='Sign in' ,
    icon='🔑' ,
)
sign_up = st.Page(
    page='Pages/signup.py',
    title='Sign up',
    icon='👤' ,
)
chat_bot = st.Page(
    page='Pages/chatbot.py' ,
    title='Ask AI' ,
    icon='🤷‍♂️' ,
)
all_Pages = st.navigation(
    pages=[home_page, products_page, sign_in, sign_up, chat_bot],
)
all_Pages.run()