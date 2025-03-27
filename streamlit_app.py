import streamlit as st
import datetime as datetime

st.set_page_config(
    page_title="My application for data",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🎈 My new aplication for data visialization")

st.header('_HI_ :green[V5s]')
st.subheader('welcome to the **class**')

st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

value=st.slider('select a value: ', 0, 100, 30)
st.write('you selected: ',value)

st.markdown('<p style="color:yellow; font-size:20;"> I should be yellow</p>', unsafe_allow_html=True)

sport_list = ['soccer','basket','golf','tennis']
button_pres=st.button('push me for sport list', type='primary')
if button_pres:
    st.write(sport_list)

check =st.checkbox('i like it')

if check:
    st.write('thank you')
else:
    st.write('Oh Nooo')

choosen_item = st.radio('what sport do you like', sport_list)

st.write('i knew you like', choosen_item)

choosen_item_2=st.selectbox('what sport do you like', sport_list)
st.write('i knew you like', choosen_item_2)

multi_item=st.multiselect('what sport do you like', sport_list)

for sports in multi_item:
    st.write(sports)

age=st.slider('your are', 18,65,[25,50])
st.write('your age is: ', age)

name_user=st.text_input('your name',placeholder='write')
st.write(name_user)

age_user=st.number_input('your age', min_value=18, max_value=65,step=1
                         )

#match_date=st.date_input('select a date',
#                         value=datetime(2025, 5, 2))

with st.form('user information'):
    name_user=st.text_input('your name',placeholder='write')
    st.write(name_user)

    age_user=st.number_input('your age', min_value=18, max_value=65,step=1
                            )
    submitted = st.form_submit_button('submitted it')

if submitted:
    st.write('submitted it great!')

