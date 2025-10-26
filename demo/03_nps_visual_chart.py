import json
import matplotlib.pyplot as plt
import os

# Define absolute path for summaries folder
summary_path = os.path.join("demo", "summaries")
os.makedirs(summary_path, exist_ok=True)

# Load data
with open(os.path.join(summary_path, "nps_summary.json")) as f:
    data = json.load(f)

promoters = data["promoters"]
detractors = data["detractors"]
passives = data.get("passives", 0)

# Chart data
labels = ["Promoters", "Passives", "Detractors"]
values = [promoters, passives, detractors]
colors = ["green", "gold", "red"]

plt.figure(figsize=(6, 4))
bars = plt.bar(labels, values, color=colors)

plt.title(f"Customer Sentiment Distribution\nNPS = {data['nps']}")
plt.xlabel("Customer Type")
plt.ylabel("Count")

# Add numbers on top of bars
for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        str(bar.get_height()),
        ha="center",
        va="bottom"
    )

plt.tight_layout()

# ✅ Save chart explicitly using absolute path
chart_path = os.path.join(summary_path, "nps_chart.png")
plt.savefig(chart_path, dpi=150)
plt.close()  # close to ensure file is written

print(f"✅ Chart saved at: {os.path.abspath(chart_path)}")

