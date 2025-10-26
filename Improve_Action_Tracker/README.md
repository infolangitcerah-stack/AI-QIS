
---

#### 📘 `Improve_Action_Tracker/README.md`
```markdown
# 🔄 Action Tracker (CPM Mini) (Improve)

Plan and monitor corrective & preventive actions.

## What it Does
- Records action, owner, status, before/after metrics
- Tracks completion vs due dates
- Summarizes improvements

## Inputs
| Field | Description |
|--------|--------------|
| `action_id` | Unique ID |
| `title` | Short action name |
| `owner` | Responsible person |
| `due_date` | Target completion |
| `status` | Open / In-Progress / Closed |
| `kpi_before` | Baseline |
| `kpi_after` | Result |

### Example
```csv
action_id,title,owner,due_date,status,kpi_before,kpi_after
A001,Add peak-hour staff,Dominic,2025-10-25,Closed,57,48
