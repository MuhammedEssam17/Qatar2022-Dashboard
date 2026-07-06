import pandas as pd
import streamlit as st


@st.chache_data
def load_data():
    df = pd.read_csv("Fifa_world_cup_matches.csv")
    df.columns = (
        df.columns.str.strip()
    )  # Remove leading/trailing whitespace from column names
    return df
