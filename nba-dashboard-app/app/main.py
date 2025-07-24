# app/main.py

import streamlit as st
import pandas as pd
import plotly.express as px
import os
from predict import predict_pts

# Load data
# Determine file path relative to this file
base_dir = os.path.dirname(__file__)
data_path = os.path.join(base_dir, '../data/cleaned_nba_data.csv')

# Load dataset
df = pd.read_csv(data_path)

# Clean column names
df = df.rename(columns={'FG%': 'FG_pct', '3P%': '3P_pct', 'FT%': 'FT_pct', 'Data': 'Date'})
df['Date'] = pd.to_datetime(df['Date'])
# Sidebar for user input
player = st.sidebar.selectbox('Select a Player:', sorted(df['Player'].unique()))

# Filter data for the selected player
player_df = df[df['Player'] == player]

st.title(f'NBA Player Performance Dashboard: {player}')

# --- Visualizations ---

st.subheader("Game-by-Game Performance")
fig = px.line(player_df, x='Date', y='PTS', title='Points Over Time')
st.plotly_chart(fig)

st.subheader("Game Stats Table")
st.dataframe(player_df[['Date', 'PTS', 'MP', 'FGA', '3PA', 'FTA', 'TRB', 'AST', 'TOV']].sort_values(by='Date', ascending=False))

# --- Prediction Section ---

st.subheader("Predict Points for a Game")

with st.form("prediction_form"):
    mp = st.number_input("Minutes Played", min_value=0.0, max_value=48.0, value=30.0)
    fga = st.number_input("Field Goal Attempts", value=15)
    fg_pct = st.slider("Field Goal %", min_value=0.0, max_value=1.0, value=0.45)
    three_pa = st.number_input("3-Point Attempts", value=5)
    three_p_pct = st.slider("3-Point %", min_value=0.0, max_value=1.0, value=0.35)
    fta = st.number_input("Free Throw Attempts", value=6)
    ft_pct = st.slider("Free Throw %", min_value=0.0, max_value=1.0, value=0.80)
    trb = st.number_input("Total Rebounds", value=5)
    ast = st.number_input("Assists", value=5)
    tov = st.number_input("Turnovers", value=2)

    submit = st.form_submit_button("Predict")

    if submit:
        input_data = pd.DataFrame([{
            'MP': mp,
            'FGA': fga,
            'FG_pct': fg_pct,
            '3PA': three_pa,
            '3P_pct': three_p_pct,
            'FTA': fta,
            'FT_pct': ft_pct,
            'TRB': trb,
            'AST': ast,
            'TOV': tov
        }])
        prediction = predict_pts(input_data)
        st.success(f"Predicted Points: **{prediction:.2f}**")