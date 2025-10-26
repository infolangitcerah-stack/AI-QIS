
---

#### 📘 `Control_5S_Audit_Tool/README.md`
```markdown
# 🧹 5S Self-Audit Tool (Control)

Maintain workplace discipline through simple self-audits.

## What it Does
- Quick checklist: Sort, Set, Shine, Standardize, Sustain
- Computes 5S score
- Shows trend & flags low areas

## Inputs
| Field | Description |
|--------|--------------|
| `date` | Audit date |
| `area` | Zone/Section |
| `S1`–`S5` | Scores (0–5) |
| `notes` | Comments |

### Example
```csv
date,area,S1,S2,S3,S4,S5,notes
2025-10-20,Front Counter,4,4,3,3,3,"Label bins; cables visible"
