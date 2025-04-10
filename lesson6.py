import streamlit as st

# call the different pages

page1 = st.Page('page1.py', title='Page 1')
page2 = st.Page('page2.py', title='Page 2')
page3 = st.Page('exercise.py', title='Page 3')

# put the pages togheder in the side bar

pg=st.navigation([page1,page2,page3])
st.set_page_config(page_title='DV4S - Exe')

# selct box
st.sidebar.selectbox(
    'select your player',
     ('Maradone', 'Paperino','Pluto'),
     key='Players', # keyboard to recoll the object
      )
# a dofferent approach with the 'with'
with st.sidebar:
    rb = st.radio(
        'Team',
        ['Napoli','Paperopoli','Milan'],
        key='Team'
    )


# we have to run the pages.
pg.run() # it shoul be put in a main page with out a graphical information.


