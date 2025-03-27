import streamlit as st

st.set_page_config(
    page_title='My application for data',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.title("🎈 My new appplication for data visialization")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

value=st.slider('select a value: ', 0, 100, 30)
st.write('you selected: ',value)