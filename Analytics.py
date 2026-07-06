import numpy as np


def analytics(df):
    # Use numpy to calculate the total number of goals of first and second team
    tt_goals1 = np.sum(df["number of goals team1"])
    tt_goals2 = np.sum(df["number of goals team2"])
    tt_goals = tt_goals1 + tt_goals2

    # Calculate the average and max and minimum number of goals scored per match with NumPy
    avg_goals = np.mean(df["number of goals team1"] + df["number of goals team2"])
    max_goals = np.max(df["number of goals team1"] + df["number of goals team2"])

    return tt_goals, avg_goals, max_goals


def filter_matches_by_stage(df, selected_stage):
    # Filter the dataframe based on the selected stage usnig pandas
    filtered_df = df[df["category"] == selected_stage].copy()
    return filtered_df


def classify_matches(filtered_df):
    goals_matrix = (
        filtered_df["number of goals team1"].to_numpy()
        + filtered_df["number of goals team2"].to_numpy()
    )
    match_classification = np.where(
        goals_matrix > 2, "High Scoring", "Defensive | Tactical game"
    )
    return match_classification
