# 🚀 How to Launch the UI

## Simple 3-Step Process:

### **Step 1: Install Dependencies**
```bash
cd "/Users/I079250/Current Work/Learning/Buildathon/incident-response-crew"

python3 -m venv .venv
source .venv/bin/activate
pip install crewai litellm openai python-dotenv streamlit
```

### **Step 2: Configure API Key (Optional)**
```bash
# Option A: Use Groq (Fast & Free)
cp .env.example .env
# Edit .env and add: GROQ_API_KEY=your_key

# Option B: Use Ollama (Local)
ollama serve
ollama pull llama3:8b
```

### **Step 3: Launch the UI** 🎉
```bash
streamlit run app.py
```

**That's it!** Your browser will automatically open to:
```
http://localhost:8501
```

---

## 🎨 What You'll See:

The UI has **3 tabs**:

### **Tab 1: Quick Scenarios** 🎯
- 3 pre-loaded test scenarios
- Click any "Analyze" button
- Watch AI agents work
- Get complete RCA report

### **Tab 2: Custom Incident** ✏️
- Enter your own incident details
- Fill in service, timeframe, description
- Click "Analyze Custom Incident"
- Get personalized RCA

### **Tab 3: About** 📊
- System overview
- How it works
- Agent descriptions
- Test scenario details

---

## 🚀 Quick Command:

```bash
cd "/Users/I079250/Current Work/Learning/Buildathon/incident-response-crew" && \
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install crewai litellm openai python-dotenv streamlit && \
streamlit run app.py
```

**Copy-paste this single command to launch everything!**

---

## 📸 What the UI Looks Like:

```
┌─────────────────────────────────────────────────────┐
│     🚨 Incident Response AI System                  │
│     AI-powered Root Cause Analysis                  │
└─────────────────────────────────────────────────────┘

  [Quick Scenarios] [Custom Incident] [About]

  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
  │ Scenario 1   │ │ Scenario 2   │ │ Scenario 3   │
  │ Deployment   │ │ Memory Leak  │ │ App Bug      │
  │              │ │              │ │              │
  │ [🔍 Analyze] │ │ [🔍 Analyze] │ │ [🔍 Analyze] │
  └──────────────┘ └──────────────┘ └──────────────┘

```

---

## 🎯 Try It Now!

**Just run:**
```bash
streamlit run app.py
```

The UI will open automatically in your browser! 🌐
