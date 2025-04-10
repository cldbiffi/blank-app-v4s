import streamlit as st

team_name='Barcellona'
seasons=['2020-21','2021-22','2022-23','2023-24']
wins=[20,22,18,25]
losses=[10,8,12,5]
goals_scored=[60,65,55,70]

top_scores={'Messi': 15, 'Pele': 12, 'Maradona': 10}

st.header(f'Player and team statistics of {team_name}')


col1, col2, col3 = st.columns([1, 1, 1])
col1.header('Select a season')
seas = col1.radio('Season', seasons)

# Get index of selected season
season_index = seasons.index(seas)

# Retrieve corresponding values for wins, losses, and goals scored
w = wins[season_index]
l = losses[season_index]
g = goals_scored[season_index]

# Display win and loss bar chart
col2.header('Wins & Losses')
col2.bar_chart([w, l],x_label='W & L',y_label= 'Goals')

# Display total goals scored
col3.header('Total Goals Scored')
col3.write(f'In the {seas} season, the team scored {g} goals.')



# Select player and show goals scored
sel = st.selectbox('Choose the player', list(top_scores.keys()), placeholder='Choose a player')
player_goals = top_scores.get(sel, 0)  # Get goals for selected player (default 0 if player not in dictionary)
st.write(f'{sel} scored {player_goals} goals in total.')


