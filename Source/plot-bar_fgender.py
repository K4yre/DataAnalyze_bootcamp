import main

df = main.df
genders = df["Gender"].dropna().unique()

for gender in genders:
    df_gender = df[df["Gender"] == gender]

    if df_gender.empty:
        continue

    main.plot_graph_bar(df_gender, title_suffix=f"Gender: {gender}")
