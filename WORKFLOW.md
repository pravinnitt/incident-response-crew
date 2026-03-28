# Incident Response System - Workflow Diagram

## 🔄 Complete System Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                     INCIDENT DETECTED                           │
│  (User runs: python main.py --scenario 1)                      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    LOAD INCIDENT DATA                           │
│  • incident_id: INC-2026-03-28-001                              │
│  • service: payment-api                                         │
│  • timeframe: 10:00 - 10:30                                     │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│               AGENT 1: LOG ANALYZER                             │
│  Role: Log Analysis Expert                                      │
│  Tools: Log Reader, Pattern Matcher                             │
│                                                                 │
│  Actions:                                                       │
│  1. Read logs: test_data/logs/payment-api-scenario1.log        │
│  2. Identify errors: 50+ database timeout errors               │
│  3. Extract patterns: All timeouts at 30 seconds               │
│  4. Build timeline: First error at 10:00:03                    │
│                                                                 │
│  Output:                                                        │
│  ✓ Error count: 50+                                             │
│  ✓ Primary error: Database connection timeout                  │
│  ✓ Anomaly: Error spike from 0.1% → 15%                        │
│  ✓ Timeline: Errors started 2 min after deployment             │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              AGENT 2: TRIAGE SPECIALIST                         │
│  Role: Incident Triage Specialist                              │
│  Context: Log analysis results                                  │
│                                                                 │
│  Actions:                                                       │
│  1. Assess severity: P1 (High)                                 │
│  2. Categorize: Application / Database                         │
│  3. Estimate impact: 1500 users affected                       │
│  4. Calculate business impact: Revenue loss                    │
│                                                                 │
│  Output:                                                        │
│  ✓ Severity: P1 - High                                          │
│  ✓ Category: Application/Database                              │
│  ✓ User Impact: 1500 users, payment failures                   │
│  ✓ Business Impact: $45K revenue loss estimate                 │
│  ✓ Escalation: Not needed (resolved)                           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ├──────────────────┬────────────────────┐
                         ▼                  ▼                    ▼
┌───────────────────────────┐  ┌─────────────────────────────────┐
│ AGENT 3: DEPLOYMENT       │  │ AGENT 2: PLAYBOOK SEARCH        │
│ CHECKER                   │  │ (Triage Agent)                  │
│                           │  │                                 │
│ Tools: Deployment History │  │ Tool: Playbook Search           │
│        Git Diff           │  │                                 │
│                           │  │ Actions:                        │
│ Actions:                  │  │ 1. Search by type: "database"   │
│ 1. Check deployments      │  │ 2. Search by keyword: "timeout" │
│ 2. Find v2.5.1 deployed   │  │ 3. Retrieve runbook             │
│    at 09:58:00            │  │                                 │
│ 3. Incident at 10:00:03   │  │ Output:                         │
│    = 2 min gap            │  │ ✓ Found: database-timeout.md    │
│ 4. Analyze changes:       │  │ ✓ Symptoms match                │
│    - Timeout 60s → 30s ⚠️  │  │ ✓ Recommends: Check timeout     │
│                           │  │              config              │
│ Output:                   │  └─────────────────────────────────┘
│ ✓ Correlation: HIGH (95%) │
│ ✓ Suspicious: Timeout     │
│    config changed         │
│ ✓ Rollback: Performed     │
│ ✓ Effective: Yes          │
└───────────────────────────┘
                         │
                         │
    ┌────────────────────┴────────────────────┐
    │                                         │
    ▼                                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                  AGENT 4: RCA EXPERT                            │
│  Role: Root Cause Analysis Expert                              │
│  Context: ALL previous task outputs                            │
│                                                                 │
│  Actions:                                                       │
│  1. Synthesize findings from all agents                        │
│  2. Build complete timeline                                    │
│  3. Apply 5 Whys methodology                                   │
│  4. Identify root cause vs symptoms                            │
│  5. Generate evidence-based conclusions                        │
│  6. Create recommendations                                     │
│                                                                 │
│  5 Whys Analysis:                                              │
│  Q1: Why did payments fail?                                    │
│  A1: Database connection timeouts                              │
│                                                                 │
│  Q2: Why did connections timeout?                              │
│  A2: Timeout set to 30 seconds                                 │
│                                                                 │
│  Q3: Why was timeout set to 30s?                               │
│  A3: Config change in deployment v2.5.1                        │
│                                                                 │
│  Q4: Why wasn't this tested?                                   │
│  A4: No load testing for config changes                        │
│                                                                 │
│  Q5: Why no load testing required?                             │
│  A5: Deployment process gap                                    │
│                                                                 │
│  Output:                                                        │
│  ✓ Root Cause: Timeout config reduced from 60s to 30s          │
│  ✓ Contributing Factors: No load testing, no canary            │
│  ✓ Evidence: 189 timeouts at exactly 30s, timing correlation  │
│  ✓ Immediate Fix: Rollback performed, effective               │
│  ✓ Short-term: Revert config, add alerts                       │
│  ✓ Long-term: Implement load testing, canary deployments      │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   GENERATE FINAL REPORT                         │
│                                                                 │
│  Report Sections:                                              │
│  1. Executive Summary                                          │
│  2. Incident Timeline                                          │
│  3. Log Analysis Summary                                       │
│  4. Severity & Impact Assessment                               │
│  5. Deployment Correlation Analysis                            │
│  6. Root Cause Analysis (5 Whys)                               │
│  7. Evidence & Supporting Data                                 │
│  8. Immediate Remediation                                      │
│  9. Prevention Recommendations                                 │
│  10. Lessons Learned                                           │
│                                                                 │
│  Output Format: Markdown + Plain Text                          │
│  Saved to: output/INC-2026-03-28-001_report.txt                │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                    ANALYSIS COMPLETE ✅                          │
│                                                                 │
│  Root Cause Identified: Configuration Error                    │
│  Time to Resolution: 18 minutes (from detection to rollback)   │
│  Confidence: HIGH (95%)                                         │
│  Recommendations: 6 short-term, 6 long-term actions            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 📊 Data Flow

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ Incident     │ ───▶ │ Scenario     │ ───▶ │ Main Entry   │
│ Occurs       │      │ JSON         │      │ Point        │
└──────────────┘      └──────────────┘      └──────┬───────┘
                                                    │
                    ┌───────────────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────┐
    │         BUILD CREW                    │
    │  • Initialize 4 agents                │
    │  • Create 5 tasks with context        │
    │  • Set up sequential process          │
    └───────────────┬───────────────────────┘
                    │
                    ▼
    ┌───────────────────────────────────────┐
    │      SEQUENTIAL TASK EXECUTION        │
    └───────────────────────────────────────┘
            │
            ├─▶ Task 1: Log Analysis
            │   └─▶ Context: Incident data
            │
            ├─▶ Task 2: Triage
            │   └─▶ Context: Task 1 output
            │
            ├─▶ Task 3: Deployment Check
            │   └─▶ Context: Task 2 output
            │
            ├─▶ Task 4: Playbook Search
            │   └─▶ Context: Task 1 & 2 output
            │
            └─▶ Task 5: RCA Generation
                └─▶ Context: ALL previous outputs
                │
                ▼
    ┌───────────────────────────────────────┐
    │       FINAL REPORT                    │
    │  Comprehensive RCA with all sections  │
    └───────────────────────────────────────┘
```

---

## 🔧 Tool Usage Flow

```
Log Reader Tool
  ├─▶ Reads: test_data/logs/{service}.log
  └─▶ Returns: Formatted log entries

Pattern Matcher Tool
  ├─▶ Analyzes: Log content
  └─▶ Returns: Error frequencies, anomalies

Deployment History Tool
  ├─▶ Reads: test_data/deployments/{service}.json
  └─▶ Returns: Deployment timeline

Git Diff Tool
  ├─▶ Analyzes: Deployment changes
  └─▶ Returns: Suspicious changes flagged

Playbook Search Tool
  ├─▶ Searches: test_data/playbooks/*.md
  └─▶ Returns: Relevant runbook content
```

---

## ⏱️ Typical Execution Time

```
Total Time: ~2-3 minutes (with Groq)

Phase 1: Log Analysis        ⏱️  30-45 seconds
  └─ Read logs, identify patterns

Phase 2: Triage              ⏱️  20-30 seconds
  └─ Assess severity, categorize

Phase 3: Deployment Check    ⏱️  20-30 seconds
  └─ Correlate with deployments

Phase 4: Playbook Search     ⏱️  15-20 seconds
  └─ Find relevant runbooks

Phase 5: RCA Generation      ⏱️  45-60 seconds
  └─ Synthesize all findings
```

---

## 💾 Memory & Context

```
Agent Memory: Disabled (memory=False)
  └─ Each run is independent

Context Passing: Enabled
  ├─ Task 1 output → Task 2
  ├─ Task 2 output → Task 3 & 4
  └─ All outputs → Task 5

LLM Context Window:
  └─ ~2000-3000 tokens per scenario
```

---

## 🎯 Success Metrics

```
✓ Error Detection:     90%+ accuracy
✓ Severity Classification: P0-P4 correct
✓ Deployment Correlation: HIGH/MEDIUM/LOW accurate
✓ Root Cause Accuracy: 80%+ actionable
✓ Report Completeness: All 10 sections present
✓ Processing Time:     < 3 minutes
✓ Recommendations:     3+ actionable items
```
