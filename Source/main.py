import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(BASE_DIR, "Data_Set", "UI UX Dataset.csv")
data = pd.read_csv(file_path)
df = pd.DataFrame(data)

flag = False
# Check DataFrame
if flag:
    # ----- Check for Nulls ----- #
    print(df.isna().sum())
    print(df.isna().sum().sum())

    # ----- Check the Data ----- #
    print(df.describe())
    print(df.info())

# ----- Variable Grouping into study categories ----- #
visual_design = ["Color Scheme", "Visual Hierarchy", "Typography", "Images and Multimedia", "Layout",
                 "Animation and Transitions"]
interaction = ["Scrolling_Behavior", "Gestures and Touch Controls", "CTA (Call to Action) Buttons",
               "Search Functionality", "Mobile Responsiveness"]
form_personalization = ["Forms and Input Fields", "Feedback and Error Messages", "Personalization",
                        "Social_Media_Integration"]
performance = ["Loading Speed", "Accessibility"]

groups = [visual_design, interaction, form_personalization, performance]
titles = ["Visual Design", "Interactions & Controls", "Forms & Personalization", "Performance & Accessibility"]

# Create percentile bins and round then
df["AgeBracket"] = pd.qcut(df["Age"], q=6).apply(lambda x: f"{int(round(x.left))}–{int(round(x.right))}")


def wrap_label_by_length(text, max_len):
    words = text.split()
    if not words:
        return text

    lines = []
    current = words[0]

    for w in words[1:]:
        if len(current) + 1 + len(w) <= max_len:
            current += " " + w
        else:
            lines.append(current)
            current = w

    lines.append(current)
    return "\n".join(lines)


def plot_graph_bar(df_, title_suffix=None):
    fig, axes = plt.subplots(2, 2, figsize=(18, 14))
    axes = axes.flatten()

    for i, cols in enumerate(groups):
        result = df_.groupby("AgeBracket", observed=True)[cols].mean().reset_index()
        plot_df = result.melt(id_vars="AgeBracket", value_vars=cols, var_name="Variable", value_name="MeanResponse")

        sns.barplot(data=plot_df, x="AgeBracket", y="MeanResponse", hue="Variable", ax=axes[i])

        # Build final title
        base_title = titles[i]
        if title_suffix:
            final_title = f"{base_title} — {title_suffix}"
        else:
            final_title = base_title

        axes[i].set_title(final_title, fontsize=14)
        axes[i].set_xlabel("Age Bracket")
        axes[i].set_ylabel("Mean Response")
        axes[i].tick_params(axis="x", rotation=0)
        axes[i].legend(title="Variable", fontsize=9)

    plt.tight_layout()
    plt.subplots_adjust(left=0.04, right=0.96, top=0.93, bottom=0.07, wspace=0.1, hspace=0.25)
    plt.show()


def plot_graph_pie(cols, df_, filter_, categories, title):
    platforms = df_["Platform"].unique()

    rows = (len(platforms) + cols - 1) // cols
    colors = plt.colormaps["tab20"](range(len(categories)))

    plt.figure(figsize=(6 * cols, 5 * rows))

    for i, platform in enumerate(platforms, 1):
        # Filter and reindex to ensure all categories appear
        subset = (df_[df_["Platform"] == platform].set_index(filter_).reindex(categories, fill_value=0))

        plt.subplot(rows, cols, i)
        plt.pie(subset["count"], labels=None, autopct="%1.1f%%", colors=colors, startangle=90)
        plt.title(platform, fontsize=13)

    # One legend for all
    plt.legend(categories, title=title, loc="center left", bbox_to_anchor=(1.02, 0.5))
    plt.tight_layout()
    plt.show()
