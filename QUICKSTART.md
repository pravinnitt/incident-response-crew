# Quick Start Guide

## 🚀 Get Started in 5 Minutes

### Step 1: Install Dependencies (2 minutes)

```bash
cd incident-response-crew

# Using uv (recommended - faster)
curl -Ls https://astral.sh/uv/install.sh | bash
uv venv --python 3.10
source .venv/bin/activate
uv pip install crewai litellm openai python-dotenv

# OR using pip
python -m venv .venv
source .venv/bin/activate
pip install crewai litellm openai python-dotenv
```

### Step 2: Configure API Key (1 minute)

**Option A: Use Groq (Recommended - Fast & Free)**
```bash
# Get free API key from: https://console.groq.com/keys
cp .env.example .env
# Edit .env and add: GROQ_API_KEY=your_key_here
```

**Option B: Use Ollama (Local - No API Key)**
```bash
# Install Ollama: https://ollama.ai/
ollama serve
ollama pull llama3:8b
# No .env needed!
```

### Step 3: Run Test (30 seconds)

```bash
# Verify everything works
python tests/test_system.py
```

### Step 4: Run Your First Incident Analysis (2 minutes)

```bash
# Analyze a deployment-related incident
python main.py --scenario 1

# Or use the quick script
./run_scenario1.sh
```

## 📊 What You'll See

The system will:
1. ✅ Analyze logs (find 50+ database timeout errors)
2. ✅ Classify as P1 severity
3. ✅ Correlate with recent deployment (HIGH confidence)
4. ✅ Find relevant playbook (database-timeout.md)
5. ✅ Generate complete RCA report with recommendations

**Output saved to**: `output/INC-2026-03-28-001_report.txt`

## 🎯 Try All Scenarios

```bash
# Scenario 1: Deployment issue (timeout config)
python main.py --scenario 1

# Scenario 2: Memory leak (infrastructure)
python main.py --scenario 2

# Scenario 3: Application bug (NullPointerException)
python main.py --scenario 3
```

## 🔧 Custom Incident

```bash
python main.py \
  --incident-id "INC-2026-001" \
  --service "payment-api" \
  --start-time "2026-03-28T10:00:00Z" \
  --end-time "2026-03-28T10:30:00Z" \
  --description "Payment failures"
```

## 🐛 Troubleshooting

**Issue**: `No module named 'crewai'`
```bash
# Make sure virtual env is activated
source .venv/bin/activate
pip install crewai litellm openai python-dotenv
```

**Issue**: `GROQ_API_KEY not found`
```bash
# Check .env file exists and has the key
cat .env
# Should show: GROQ_API_KEY=gsk_...
```

**Issue**: `Ollama connection failed`
```bash
# Make sure Ollama is running
ollama serve
ollama pull llama3:8b
```

## 📖 Next Steps

- Read `README.md` for full documentation
- Customize agents in `src/agents/`
- Add your own test data in `test_data/`
- Modify tools in `src/tools/`

## 💡 Tips

- **First run takes longer** - Models need to load
- **Use Groq for speed** - Much faster than local Ollama
- **Check output folder** - All reports saved there
- **Verbose mode** - See detailed agent thinking

---

**Need Help?** Check README.md or open an issue!
