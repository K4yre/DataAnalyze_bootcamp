import main

df = main.df

# ----- Reaction Map ----- #
reaction_map = {
    # Negative
    "Confusing": "Negative Reaction",
    "Inconsistent Navigation": "Negative Reaction",
    "Limited Menu Options": "Negative Reaction",

    # Neutral
    "Adequate": "Neutral Reaction",

    # Positive
    "Clear and concise": "Positive Reaction",
    "Efficient": "Positive Reaction",
    "Engaging": "Positive Reaction",
    "Intuitive": "Positive Reaction",
    "User-Friendly": "Positive Reaction",
    "Well-structured": "Positive Reaction"
}

df["Reaction_Group"] = df["User_experience"].map(reaction_map)

filter_table = (df.groupby(["Platform", "Reaction_Group"]).size().reset_index(name="count"))

categories = ["Negative Reaction", "Neutral Reaction", "Positive Reaction"]
title = "User Experience Groups"

main.plot_graph_pie(3, filter_table, "Reaction_Group", categories, title)
