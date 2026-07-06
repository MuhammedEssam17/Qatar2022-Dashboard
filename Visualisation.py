import streamlit as st
import matplotlib.pyplot as plt


def display_possession_analysis(filtered_df):
    """Create visual progress bars and Pie chart to display possession analysis for match possession"""
    st.markdown("------")
    st.subheader("Match dynamics and style analysis")

    if not filtered_df.empty:
        # Selectbox to choose a specific match from the filtered dataframe
        match_titles = [
            f"{row['team1']} vs {row['team2']}" for _, row in filtered_df.iterrows()
        ]
        selected_match_name = st.selectbox(
            "Select a match to analyze possession: ", match_titles
        )

        match_index = match_titles.index(selected_match_name)
        selected_match = filtered_df.iloc[match_index]

        # To extract possession values and convert them to integers, removing the percentage sign
        pos_t1 = int(str(selected_match["possession team1"]).replace("%", ""))
        pos_t2 = int(str(selected_match["possession team2"]).replace("%", ""))
        pos_contest = int(str(selected_match["possession in contest"]).replace("%", ""))

        # Display quick progress bar using streamlit
        st.markdown("### Match Score and possession ")
        col_p1, col_p2, col_p3 = st.columns(3)

        with col_p1:
            st.markdown(f"### **{selected_match['team1']}**")
            st.metric(label="Goals", value=int(selected_match["number of goals team1"]))
            st.caption(f"Possession: {pos_t1}%")
            st.progress(pos_t1)

        with col_p2:
            st.markdown(f"### **VS**")
            st.metric(label="In Contest", value=f"{pos_contest}%")
            st.progress(pos_contest)

        with col_p3:
            st.markdown(f"### **{selected_match['team2']}**")
            st.metric(label="Goals", value=int(selected_match["number of goals team2"]))
            st.caption(f"Possession: {pos_t2}%")
            st.progress(pos_t2)

        st.markdown("-----")

        # Create a pie cahrt with matplotlib
        st.write("Visual Possession Pie Chart")

        lables = [selected_match["team1"], selected_match["team2"], "In Contest"]
        sizes = [pos_t1, pos_t2, pos_contest]
        colors = ["#8A1538", "#EE7C11", "#A6A6A6"]

        # Prepare the pie chart with matplotlib
        fig = plt.figure(figsize=(4, 3))
        ax = fig.add_subplot(1, 1, 1)

        ax.pie(
            sizes,
            labels=lables,
            colors=colors,
            autopct="%1.1f%%",
            startangle=140,
            textprops={"color": "white"},
            radius=0.8,
        )

        fig.patch.set_alpha(0.0)
        ax.patch.set_alpha(0.0)

        col_left, col_center, col_right = st.columns([2, 1.5, 2])

        with col_center:
            st.pyplot(fig, width="stretch")
