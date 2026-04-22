import streamlit as st
st.title('welcome to our store',
         text_alignment='center')
st.subheader('the most trusted products in the world',
             text_alignment='center')
st.image('Images/main.png',
         width=1000,)
st.divider()
#Not professional method to divide the page#
left, right = st.columns(2, border=True, )
#left.subheader('Browse our great K products')
#left.write('find out the best K products')
#left.button('Browse')
#right.subheader('Need help?')
#right.write('Ask our chatbot')
#right.button('Ask AI')
with left:
    st.subheader('Browse our K products')
    st.write('find out the best K products')
    if st.button('Browse',
                 use_container_width=True):
        st.switch_page('Pages/products.py')
with right:
    st.subheader('Need help?')
    st.write('Ask our chatbot')
    if st.button('Ask AI ✨',
                 use_container_width=True):
        st.switch_page('Pages/chatbot.py')
