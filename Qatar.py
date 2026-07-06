import streamlit as st
from Visualisation import display_possession_analysis
from Data_loader import load_data
from Analytics import analytics, filter_matches_by_stage, classify_matches

# Handle the page layout and configuration
st.set_page_config(
    page_title="Fifa World Cup Matches Data Analytics",
    page_icon="🏆",
    layout="wide",
)
st.title("🏆 FIFA World Cup Matches Data Analytics")
st.markdown("-----")

# Load the data
df = load_data()

# Display the tournament states overview
st.subheader("📊 Tournament Overview")
tt_goals, avg_goals, max_goals = analytics(df)

# Display the tournament statistics in a 3-column layout
col1, col2, col3 = st.columns(3)
col1.metric("Total Tournament Goals", value=int(tt_goals))
col2.metric("Tournament Average Goals", value=f"{avg_goals:.2f}")
col3.metric("Tournament Max Goals", value=int(max_goals))
st.markdown("-----")

# Filter matches by stage and display the filtered dataframe
st.subheader("🔍 Filter Matches by Stage")

# Get a unique list of stages from the 'category' column and sort them
stages = sorted(df["category"].unique())
selected_stage = st.selectbox("select a stage / group", stages)

# Filter the dataframe based on the selected stage using pandas
filtered_df = filter_matches_by_stage(df, selected_stage)


if not filtered_df.empty:
    # Apply Numpy classification Logic
    filtered_df["Match Classification"] = classify_matches(filtered_df)

    # select specific column to display in the main table
    display_cols = [
        "date",
        "team1",
        "number of goals team1",
        "team2",
        "number of goals team2",
        "Match Classification",
    ]
    # To make the interface more attractive, won't display the table if there is only one match like the final match.
    if len(filtered_df) > 1:
        st.dataframe(filtered_df[display_cols], hide_index=True, width="stretch")
    else:
        st.info("🎯 Single match stage - check the live scoreboard below!")
    # Call visualization function to display possession analysis for the filtered dataframe
    display_possession_analysis(filtered_df)
else:
    st.warning("No matches found for the selected stage.")
