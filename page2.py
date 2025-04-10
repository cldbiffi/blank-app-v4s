import streamlit as st
import numpy as np

st.title('Page 2')

 # get information from the sidebar with the keys

st.title('get infor from sidebar')


# usefull also to share infrmations 
player=st.session_state['Players']
team=st.session_state['Team']

st.write('the player is: ', player)
st.write('the team is: ', team)


# column it return a list of containes that so i have to use methods for the containers
st.title('we use coloum')
col1,col2 = st.columns(2)

# sp npw i can use the with ir the object notation

col1.header('This is coloum 1')

st.title('More coloums')
data=np.random.rand(20,1)

colA,colB = st.columns([3,1])

with colA:
    st.header('Data Viz')
    st.bar_chart(data)

with colB:
    st.header('Table')
    st.table(data)


# Tabs this metods return a list of containers
st.title('here we are using tabs')
tab1, tab2= st.tabs(['gravel','road'])
tab1.subheader('GRAVEL')
tab2.subheader('ROAD')
tab1.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTosyfeKWk9ElAjNxvEJWnAawRyAN5_ftXdyA&s')
tab2.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3tAX7xVT23TRk1qv8WoECJo2UaQs9gVNWfw&s')

# exspanders

st.title('worling with the espanders')
with st.expander('Data Viz', expanded=True):
    st.subheader('My data')
    st.line_chart(data)

with st.expander('Table',expanded=False):
    st.subheader('Table')
    st.table(data)


# secrets and get information from them
st.title('display some secrets')
#username = st.secrets['general']['username']
#st.write(username)

import os

#password = os.environ['psw']
#st.write(password)

#secrets_psw=os.secrets.further_secrets.secrets_username
#st.write(secrets_psw)

# these secrets are not available for all in particular in the application

import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import pandas as pd

# Setup Google Sheets credentials
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("path_to_your_credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet by name or URL
sheet = client.open('your_google_sheet_name').sheet1

# Read specific columns and rows from the sheet
data = sheet.get_all_values()

# Convert the data to a pandas DataFrame (you can adjust column indexes as needed)
df = pd.DataFrame(data[1:], columns=data[0])

# Display the data in Streamlit
st.dataframe(df)

# Save the DataFrame as a CSV file
cwd = os.getcwd()
filename2save = os.path.join(cwd, 'data2save.csv')

df.to_csv(filename2save, index=False)

# Confirm the file was saved
st.success(f'File saved as {filename2save}')
