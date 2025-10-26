import json, os

# Load NPS summary
with open("demo/summaries/nps_summary.json") as f:
    nps_summary = json.load(f)

nps = nps_summary["nps"]
themes = nps_summary["themes"]
passives = nps_summary.get("passives", 0)
total = nps_summary["total_responses"]

# Suggest actions based on themes
if "waiting time" in themes:
    suggestion = "🕒 Add one more staff during lunch hour to reduce waiting time."
elif "clean" in themes:
    suggestion = "🧽 Increase cleaning frequency between shifts."
elif "staff" in themes:
    suggestion = "👥 Provide refresher training on customer interaction."
else:
    suggestion = "✅ Maintain current process and monitor weekly."

# Analyze Passive ratio
passive_ratio = round((passives / total) * 100, 1)
if passive_ratio > 20:
    passive_note = f"🟡 {passive_ratio}% of customers are passive — they like your service but aren’t yet loyal. Focus on delighting them with small improvements."
else:
    passive_note = f"Only {passive_ratio}% of customers are passive — good balance of engagement."

# Build AI Insight Report
report = {
    "headline": f"NPS is {nps}. Top themes: {', '.join(themes)}.",
    "ai_suggestion": suggestion,
    "ai_passive_insight": passive_note
}

# Save to file
os.makedirs("demo/summaries", exist_ok=True)
with open("demo/summaries/ai_insight_output.json", "w") as f:
    json.dump(report, f, indent=2)

print("🤖 AI Insight Report:")
print(json.dumps(report, indent=2))

