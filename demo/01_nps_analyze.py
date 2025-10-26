import pandas as pd
import json
import os

# Ensure summaries folder exists
os.makedirs("demo/summaries", exist_ok=True)

# Load data
df = pd.read_csv("demo/data/nps_sample.csv")

# Classify each score
def classify(score):
    if score >= 9:
        return "Promoter"
    elif score <= 6:
        return "Detractor"
    else:
        return "Passive"

df["category"] = df["score"].apply(classify)

# Calculate NPS and counts
promoters = int((df["category"] == "Promoter").sum())
detractors = int((df["category"] == "Detractor").sum())
passives = int((df["category"] == "Passive").sum())
total = int(len(df))
nps = int(round(((promoters - detractors) / total) * 100))

# ✅ Define themes BEFORE using them
themes = []
text = " ".join(df["comment"].str.lower())
for keyword in ["waiting time", "friendliness", "clean", "speed", "staff"]:
    if keyword in text:
        themes.append(keyword)

# Build summary
summary = {
    "nps": nps,
    "promoters": promoters,
    "detractors": detractors,
    "passives": passives,
    "total_responses": total,
    "themes": themes
}

# Ensure all data types are JSON safe
summary = json.loads(json.dumps(summary, default=str))

# Save summary file
with open("demo/summaries/nps_summary.json", "w") as f:
    json.dump(summary, f, indent=2)

print("✅ NPS summary generated:")
print(json.dumps(summary, indent=2))

