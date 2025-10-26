# ⏱️ Cycle Time Tracker (Measure)

Measure lead or service time (start → finish) and visualize variation.

## What it Does
- Calculates cycle time (minutes/hours/days)
- Summarizes avg, median, p90
- Generates histogram + trend chart (future)

## Inputs
CSV/JSON with:
| Field | Description |
|--------|--------------|
| `ticket_id` | Optional ID |
| `start_ts` | Start timestamp |
| `end_ts` | End timestamp |
| `stage` | Optional process stage |

### Example
```csv
ticket_id,start_ts,end_ts
T001,2025-10-20 08:10,2025-10-20 09:05
T002,2025-10-20 08:40,2025-10-20 09:50
