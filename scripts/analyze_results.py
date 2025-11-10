import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/search_simulation_results.csv")

# Example: plot counts
df.groupby("source")["is_relevant"].sum().plot(kind="bar", title="Relevant Results Found")
plt.xlabel("Data Source")
plt.ylabel("Relevant Results")
plt.tight_layout()
plt.savefig("results/relevance_comparison.png")
