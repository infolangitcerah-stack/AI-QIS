
---

#### 📘 `AI_Insight_Panel/README.md`
```markdown
# 🤖 AI Insight Panel (Cross-Module Learning)

Integrate all module summaries to produce continuous insight.

## What it Does
- Reads outputs from Define → Measure → Analyze → Improve → Control
- Generates unified “State of Quality” summary
- Suggests top improvement focus areas

## Inputs
| File | Content |
|------|----------|
| `nps_summary.json` | NPS & themes |
| `cycle_time_summary.json` | avg/median/p90 |
| `rca_summary.json` | root cause |
| `actions_summary.json` | open/closed counts |
| `5s_summary.json` | scores |

### Example JSON
```json
{
  "nps": 62,
  "themes": ["waiting time", "friendliness"],
  "cycle_time_avg_min": 57,
  "root_cause": "Roster not aligned",
  "actions_open": 3,
  "five_s_score": 3.4
}
