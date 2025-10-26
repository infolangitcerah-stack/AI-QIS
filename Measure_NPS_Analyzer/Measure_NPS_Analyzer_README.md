# 📊 Measure Phase — AI-NPS Analyzer
*Part of the AI Quality Intelligence Suite (AI-QIS) – applying DMAIC principles to empower SMEs.*

---

## 🧭 PHASE OVERVIEW
The **Measure Phase** focuses on capturing, quantifying, and visualizing customer satisfaction and loyalty through the **AI-NPS Analyzer**.  
This is where we move from the *Define* phase’s vision into *measurable data*, enabling SMEs to see customer sentiment and trends in real time.

> “If you can’t measure it, you can’t improve it.” – Peter Drucker  

---

## 🧩 Purpose of the AI-NPS Analyzer
The **AI-NPS Analyzer** helps SMEs transform unstructured customer feedback into structured data that supports decision-making and quality improvement.  
It calculates:
- Net Promoter Score (NPS)  
- Sentiment-based themes (AI-derived)  
- Visual distribution charts  
- Insights for improvement planning  

---

## ⚙️ Folder Structure
```
Measure_NPS_Analyzer/
├── nps_sample.csv              # Dummy dataset of customer feedback
├── 01_nps_analyze.py           # Calculates NPS and extracts themes
├── 02_ai_insight_panel.py      # Generates AI insights (optional)
├── 03_nps_visual_chart.py      # Creates visual representation
├── summaries/
│   ├── nps_summary.json        # NPS result summary
│   ├── ai_insight_output.json  # AI suggestions
│   └── nps_chart.png           # Chart visualization
└── README.md                   # This file
```

---

## 🧪 How It Works

### 🧾 Step 1 — Input Data
The sample file `nps_sample.csv` contains:
| Customer | Score | Feedback |
|-----------|--------|-----------|
| John | 9 | Great staff and clean environment |
| Sara | 6 | Waiting time too long |
| Ravi | 10 | Friendly and fast |
| Mei | 7 | Could improve product packaging |

---

### ⚙️ Step 2 — Run Analysis
```bash
cd "C:\Users\Dominic Belavendram\AI-QIS"
python Measure_NPS_Analyzer\01_nps_analyze.py
```

✅ Output:
```json
{
  "nps": 25,
  "promoters": 2,
  "detractors": 1,
  "passives": 1,
  "themes": ["waiting time", "clean", "staff"]
}
```

---

### 🧠 Step 3 — Generate Insights (Optional)
```bash
python Measure_NPS_Analyzer\02_ai_insight_panel.py
```

💡 Output:
```json
{
  "insight": "Customers appreciate cleanliness and staff friendliness but highlight long waiting times."
}
```

---

### 📈 Step 4 — Create Chart
```bash
python Measure_NPS_Analyzer\03_nps_visual_chart.py
```

🎨 Output:  
`nps_chart.png`

**Example Visualization (embedded):**  
![NPS Chart](summaries/nps_chart.png)

---

## 🧾 Key Learnings
| Metric | Meaning | Target |
|---------|----------|---------|
| **NPS** | %Promoters – %Detractors | Aim for +30 or higher |
| **Themes** | AI-identified improvement areas | Review weekly |
| **Passives** | Neutral customers | Convert into promoters via action plans |

---

## 🔗 Phase Navigation

### 🪜 Previous Phase  
📜 [View Project Charter →](../Define_Project_Charter/Project_Charter.md)

### 🔮 Next Phase  
🧠 [Go to Analyze Phase (AI-RCA / 5 Whys) →](../Analyze_RCA_5Whys/README.md)

---

## ✍️ Document Version
- **File:** README.md  
- **Phase:** MEASURE  
- **Version:** 1.1  
- **Date:** October 2025  
- **Authors:** Dominic Belavendram & Architect Buddy 🤝  
