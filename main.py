import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load NHANES cholesterol and demographics data (XPT format)
tchol = pd.read_sas("data/tchol.xpt")
demo = pd.read_sas("data/demo.xpt")

# Merge datasets on unique respondent ID
df = pd.merge(tchol, demo, on="SEQN")


# Filter for males aged 55
filtered_df = df[(df["RIDAGEYR"] == 55) & (df["RIAGENDR"] == 1)]

# Extract cholesterol values (mg/dL)
cholesterol_values = filtered_df["LBXTC"].dropna()


plt.figure(figsize=(10, 6))
sns.histplot(cholesterol_values, bins=30, kde=True, color="skyblue", stat="percent")
plt.ylabel("Percentage of Individuals")
plt.axvline(184, color="red", linestyle="--", linewidth=2)
plt.annotate(
    "184 mg/dL",
    xy=(184, 10),
    xytext=(190, 12),
    arrowprops=dict(facecolor="red", shrink=0.05),
    fontsize=12,
    color="red",
)
plt.title("Distribution of Total Cholesterol\nMales Aged 55 (NHANES)")
plt.xlabel("Total Cholesterol (mg/dL)")
plt.ylabel("Number of Individuals")
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("cholesterol_distribution.png")
