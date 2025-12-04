import main
import seaborn as sns
import matplotlib.pyplot as plt

# ----- Remap table ----- #
remap_table = {
    "CTA (Call to Action) Buttons": "CTA Buttons",
    "Scrolling_Behavior": "Scrolling",
    "Gestures and Touch Controls": "Gestures",
    "Forms and Input Fields": "Forms",
    "Feedback and Error Messages": "Feedback",
    "Social_Media_Integration": "Social Media"
}

df = main.df
titles = main.titles
groups = main.groups

# ----- Answer Distribution ----- #
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

for ax, cols, title in zip(axes.flatten(), groups, titles):

    plot_df = df[cols].melt(var_name="Variable", value_name="Score")
    plot_df["Variable"] = plot_df["Variable"].replace(remap_table)

    sns.violinplot(data=plot_df, x="Variable", y="Score", ax=ax)

    ax.set_title(title, fontsize=14)
    ax.set_xlabel("")
    ax.set_ylabel("Score")
    ax.tick_params(axis='x', rotation=0, labelsize=10)

    # Get current tick labels (text), wrap them by length, and set them back
    orig_labels = [t.get_text() for t in ax.get_xticklabels()]
    wrapped = [main.wrap_label_by_length(lbl, 15) for lbl in orig_labels]

    ticks = ax.get_xticks()
    ax.set_xticks(ticks)
    ax.set_xticklabels(wrapped)
plt.subplots_adjust(top=0.92, bottom=0.08, hspace=0.35)
plt.show()
