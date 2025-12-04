import main

df = main.df
platforms = df["Platform"].dropna().unique()

for platform in platforms:
    df_platform = df[df["Platform"] == platform]

    if df_platform.empty:
        continue

    main.plot_graph_bar(df_platform, title_suffix=platform)
