# Incident Response AI System

A multi-agent AI system built using CrewAI that automates incident response analysis through specialized agents working collaboratively.

## 🎯 Overview

This system simulates an incident response team with four specialized AI agents:

1. **Log Analysis Agent** - Analyzes logs for errors, patterns, and anomalies
2. **Triage Agent** - Assesses severity, categorizes incidents, and estimates impact
3. **Deployment Checker Agent** - Correlates incidents with recent deployments
4. **RCA Agent** - Synthesizes findings to determine root cause and recommendations

## 🏗️ Architecture

```
Incident Input
     ↓
[Log Analysis Agent] → Analyze logs, identify errors
     ↓
[Triage Agent] → Assess severity & categorize
     ↓
[Deployment Checker] → Check recent deployments
     ↓
[Playbook Consultation] → Find relevant runbooks
     ↓
[RCA Agent] → Generate comprehensive RCA report
     ↓
Final Report (Markdown + JSON)
```

## 🌐 Launch Web UI (Recommended)

### Quick Launch:
```bash
cd incident-response-crew
python3 -m venv .venv
source .venv/bin/activate
pip install crewai litellm openai python-dotenv streamlit
streamlit run app.py
```

The UI will open at **http://localhost:8501** 🎉

### Features:
- ✅ Pre-loaded test scenarios (just click to analyze!)
- ✅ Custom incident form
- ✅ Beautiful report visualization
- ✅ Real-time agent progress

---

## 🚀 Quick Start (CLI)

### 1. Install Dependencies

Using `uv` (recommended):
```bash
curl -Ls https://astral.sh/uv/install.sh | bash
uv venv --python 3.10
source .venv/bin/activate
uv pip install -r pyproject.toml
```

Or using pip:
```bash
python -m venv .venv
source .venv/bin/activate
pip install crewai litellm openai python-dotenv
```

### 2. Configure Environment

```bash
cp .env.example .env
# Edit .env and add your API key
```

Options:
- GROQ_API_KEY - For Groq (llama-3.1-8b-instant) - Recommended
- OPENAI_API_KEY - For OpenAI (gpt-4o-mini)
- Or use local Ollama (no key needed)

### 3. Run Test Scenarios

```bash
# Scenario 1: Deployment-related incident (database timeout)
python main.py --scenario 1

# Scenario 2: Infrastructure incident (memory leak)
python main.py --scenario 2

# Scenario 3: Application bug (NullPointerException)
python main.py --scenario 3
```

### 4. Run Custom Incident

```bash
python main.py \
  --incident-id "INC-2026-001" \
  --service "payment-api" \
  --environment "production" \
  --start-time "2026-03-28T10:00:00Z" \
  --end-time "2026-03-28T10:30:00Z" \
  --description "Payment failures reported"
```

## 📂 Project Structure

```
incident-response-crew/
├── main.py                          # Entry point
├── pyproject.toml                   # Dependencies
├── README.md                        # This file
├── .env.example                     # Environment template
├── src/
│   ├── config.py                    # LLM configuration
│   ├── crew.py                      # Crew orchestration
│   ├── agents/
│   │   ├── log_analyzer.py          # Log analysis agent
│   │   ├── triage_agent.py          # Incident triage agent
│   │   ├── deployment_checker.py    # Deployment correlation agent
│   │   └── rca_agent.py             # Root cause analysis agent
│   ├── tasks/
│   │   ├── log_analysis_task.py     # Log analysis task
│   │   ├── triage_task.py           # Triage task
│   │   ├── deployment_task.py       # Deployment check task
│   │   ├── playbook_task.py         # Playbook consultation task
│   │   └── rca_task.py              # RCA task
│   └── tools/
│       ├── log_tools.py             # Log reading and pattern matching
│       ├── deployment_tools.py      # Deployment history and git diff
│       └── playbook_tools.py        # Playbook search
├── test_data/
│   ├── logs/                        # Sample log files
│   │   ├── payment-api-scenario1.log
│   │   ├── user-service-scenario2.log
│   │   └── order-service-scenario3.log
│   ├── deployments/                 # Sample deployment history
│   │   ├── payment-api.json
│   │   ├── user-service.json
│   │   └── order-service.json
│   ├── playbooks/                   # Sample runbooks
│   │   ├── database-timeout.md
│   │   ├── memory-leak.md
│   │   └── null-pointer-exception.md
│   └── incidents/                   # Test scenarios
│       ├── scenario1.json
│       ├── scenario2.json
│       └── scenario3.json
└── output/                          # Generated reports
```

## 🧪 Test Scenarios

### Scenario 1: Deployment-Related Incident
**Description**: Database timeout configuration changed from 60s to 30s causing payment failures

**Expected Output**:
- HIGH deployment correlation
- Root cause: Configuration change
- Recommendation: Rollback and increase timeout

### Scenario 2: Infrastructure Incident
**Description**: Memory leak in UserCache causing CPU spike and OutOfMemory

**Expected Output**:
- LOW deployment correlation (no recent deployment)
- Root cause: Memory leak in cache
- Recommendation: Add cache eviction policy

### Scenario 3: Application Bug
**Description**: NullPointerException when processing orders with null shipping address

**Expected Output**:
- LOW deployment correlation
- Root cause: Missing null check
- Recommendation: Add null validation

## 📊 Output Format

The system generates comprehensive RCA reports including:

1. **Executive Summary** - One-line root cause statement
2. **Incident Timeline** - Chronological sequence of events
3. **Log Analysis** - Error patterns and frequencies
4. **Severity Assessment** - P0-P4 classification with impact
5. **Deployment Correlation** - Correlation confidence and evidence
6. **Root Cause Analysis** - 5 Whys breakdown with evidence
7. **Remediation** - Actions taken and effectiveness
8. **Prevention Recommendations** - Short-term and long-term actions
9. **Lessons Learned** - Process improvements

Reports are saved to `output/` directory.

## 🛠️ Customization

### Adding New Tools

Create tools in `src/tools/`:

```python
from crewai_tools import tool

@tool("My Custom Tool")
def my_tool(param: str) -> str:
    """Tool description"""
    # Implementation
    return result
```

### Adding New Agents

Create agents in `src/agents/`:

```python
from crewai import Agent
from src.config import get_llm

def get_my_agent():
    return Agent(
        role="My Role",
        goal="My goal",
        backstory="My backstory",
        tools=[my_tool],
        llm=get_llm(),
        verbose=True
    )
```

### Adding Test Data

Add your own test data:
- Logs: `test_data/logs/your-service.log`
- Deployments: `test_data/deployments/your-service.json`
- Playbooks: `test_data/playbooks/your-playbook.md`
- Scenarios: `test_data/incidents/your-scenario.json`

Update tool mappings in `src/tools/` to include your services.

## 🔍 Troubleshooting

### LLM Connection Issues

If using Ollama locally:
```bash
# Start Ollama
ollama serve

# Pull llama3 model
ollama pull llama3:8b
```

### Tool Execution Errors

Check that test data files exist and paths are correct in tool implementations.

### Memory Issues

For large log files, consider:
- Filtering logs by time range
- Sampling log entries
- Increasing Python memory limit

## 📈 Performance Metrics

Expected processing times (with Groq):
- Scenario 1: ~2-3 minutes
- Scenario 2: ~2-3 minutes
- Scenario 3: ~2-3 minutes

The system processes tasks sequentially to maintain context flow.

## 🎓 Learning Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [CrewAI Tools](https://github.com/joaomdmoura/crewai-tools)
- [Incident Response Best Practices](https://www.pagerduty.com/resources/learn/incident-response-process/)

## 🤝 Contributing

Feel free to:
- Add new test scenarios
- Improve agent prompts
- Add new tools
- Enhance playbooks
- Optimize performance

## 📝 License

MIT License

## 🙏 Acknowledgments

Built with:
- CrewAI - Multi-agent orchestration
- LiteLLM - Unified LLM interface
- Groq - Fast LLM inference

---

**Ready to analyze incidents?** Run `python main.py --scenario 1` to get started!
