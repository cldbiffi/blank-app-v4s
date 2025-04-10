import streamlit as st

# first part of the lesson i loose it, i can also add a icon (icon=....)

st.error('this is an error')

# warning is just a flag to say to pay attention
st.warning('this is a warning')
# success
st.success('this is a success')

st.info('this is a info')

# when i have to wait the code it is used a spinning circle or a progress bar

st.title('progress bar')

progress_bar = st.progress(0)

import time as t


for i in range(0,101):
    t.sleep(0.05)
    progress_bar.progress(i)
    # here the computational code happen

st.success('the progress end')


# spinner
st.title('spinner')

with st.spinner('running...',show_time=True):
    t.sleep(5)
st.success('end of the computation')

# side bar is where i can enter the differet page in my pplication. i can define the side bar with different
# notation, i can define it as an pbject, or use a keybouard. 
