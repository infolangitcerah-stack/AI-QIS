
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
