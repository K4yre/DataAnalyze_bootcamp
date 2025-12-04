import main

df = main.df
# Count responses by Platform and User Experience
filter_table = (df.groupby(["Platform", "User_experience"]).size().reset_index(name="count"))

categories = sorted(df["User_experience"].dropna().unique())
title = "User Experience Categories"

main.plot_graph_pie(3, filter_table, "User_experience", categories, title)
