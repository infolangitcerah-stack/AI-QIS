# 🧭 AI-NPS Analyzer (Define)

Turn raw customer feedback into a clear Net Promoter Score (NPS) and top themes.

## What it Does
- Collects simple NPS responses (0–10) + free-text comments  
- Calculates NPS (Promoters − Detractors)  
- Extracts top themes (manual tags now; AI later)

## Inputs
CSV or JSON with columns/fields:
| Field | Description |
|--------|--------------|
| `date` | Feedback date |
| `customer_id` | Optional ID |
| `score` | 0 – 10 rating |
| `comment` | Free-text comment |

### Example
```csv
date,customer_id,score,comment
2025-10-20,C001,9,"Staff were friendly, quick service"
2025-10-19,C002,5,"Long waiting time"
2025-10-18,C003,10,"Great experience!"
