
---

#### 📘 `Analyze_AI-RCA_5Whys/README.md`
```markdown
# 🧠 AI-RCA / 5 Whys Assistant (Analyze)

Structured root-cause analysis assistant.

## What it Does
- Guides “Why → Because” logic
- Records cause chain
- Identifies probable root cause(s)

## Inputs
Problem statement + list of 5 whys (manual now).

### Example
```yaml
problem: "Customers waiting too long."
whys:
  - why: "Why wait long?" because: "Orders bunch at peak."
  - why: "Why bunch?" because: "Only one counter open."
  - why: "Why one counter?" because: "Roster not aligned."
# 🔍 Analyze Phase – AI-RCA 5 Whys Assistant  

**Goal:** Identify and understand the root causes behind key NPS themes using the classical 5 Whys approach — enhanced with AI logic.  
This bridges the **Measure** insights into actionable **Analyze** learnings within the AI-QIS DMAIC framework.

---

## 🧠 Concept Overview  

| Step | Description |
|------|--------------|
| 🎯 Input | NPS summary data (themes from Measure phase) |
| ⚙️ Process | AI-driven reasoning using the 5 Whys technique |
| 📊 Output | JSON file listing each theme with its chain of “Whys” and derived root cause |

---

## 📂 Folder Structure  

Analyze_RCA_5Whys/
│
├── 01_ai_rca_5whys.py # Python script for RCA
├── input/
│ └── nps_summary.json # From Measure phase
├── output/
│ └── rca_result.json # AI-generated root cause analysis
└── README.md


---

## 🧩 Sample Output  

```json
[
  {
    "theme": "waiting time",
    "why_chain": [
      "Why 1: Customers report long waiting times during peak hours.",
      "Why 2: No dedicated staff handling queues.",
      "Why 3: Staff multitasking between cashier and prep duties.",
      "Why 4: Scheduling does not match demand.",
      "Why 5: No system for tracking real-time customer flow.",
      "Root Cause: Inefficient resource allocation during peak demand."
    ]
  }
]
💡 SME Insight Example

“Our customers mention waiting time, cleanliness, and staff behavior.
The AI-5 Whys suggests that unclear scheduling and training gaps are core issues — guiding our next Improve Phase actions.”

🧭 Navigation

⬅️ Measure Phase – NPS Analyzer

➡️ Improve Phase – Action Tracker (CPM Mini)

Part of the AI-QIS Project – Turning Feedback into Actionable Intelligence for SMEs 🚀
