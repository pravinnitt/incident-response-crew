import streamlit as st
import sys
import os
from datetime import datetime
import json

# Add src to path
sys.path.insert(0, os.path.dirname(__file__))

from src.crew import build_incident_response_crew
from src.rate_limiter import groq_rate_limiter

# Page config
st.set_page_config(
    page_title="Incident Response AI",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #FF4B4B;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-size: 1.2rem;
        padding: 0.75rem;
        border-radius: 8px;
    }
    .scenario-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 5px solid #FF4B4B;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚨 Incident Response AI System</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-powered Root Cause Analysis with Multi-Agent Collaboration</p>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/critical-thinking.png", width=80)
    st.title("🤖 System Info")
    st.markdown("""
    **Agents:**
    - 🔍 Log Analyzer
    - 🎯 Triage Specialist
    - 🚀 Deployment Checker
    - 📊 RCA Expert

    **Capabilities:**
    - Log Analysis
    - Severity Assessment (P0-P4)
    - Deployment Correlation
    - 5 Whys RCA
    - Automated Recommendations
    """)

    st.divider()

    # Rate limit status
    try:
        usage = groq_rate_limiter.get_current_usage()
        tokens_used = usage['tokens_used']
        tokens_limit = usage['tokens_limit']
        tokens_available = usage['tokens_available']
        usage_pct = (tokens_used / tokens_limit) * 100

        st.markdown("**⚡ API Rate Limit:**")
        st.progress(usage_pct / 100)
        st.caption(f"{tokens_used:,} / {tokens_limit:,} tokens used")

        if tokens_available < 1000:
            st.warning("⚠️ Low tokens available")
        elif tokens_available < 2000:
            st.info("ℹ️ Rate limit approaching")
    except:
        pass

    st.divider()
    st.markdown("**Tech Stack:**")
    st.markdown("- CrewAI")
    st.markdown("- LiteLLM + Groq")
    st.markdown("- Python 3.10+")

# Main content
tab1, tab2, tab3 = st.tabs(["🎯 Quick Scenarios", "✏️ Custom Incident", "📊 About"])

with tab1:
    st.header("Pre-loaded Test Scenarios")
    st.write("Select a scenario to analyze with AI agents")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="scenario-box">
        <h3>📦 Scenario 1</h3>
        <p><strong>Deployment Issue</strong></p>
        <p>Database timeout configuration changed causing payment failures</p>
        <ul>
        <li>Service: payment-api</li>
        <li>Severity: P1</li>
        <li>Impact: 1500 users</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔍 Analyze Scenario 1", key="s1"):
            with st.spinner("🤖 AI Agents analyzing incident..."):
                try:
                    # Load scenario
                    with open("test_data/incidents/scenario1.json", 'r') as f:
                        incident_data = json.load(f)

                    # Run crew
                    crew = build_incident_response_crew(incident_data)
                    result = crew.kickoff()

                    st.success("✅ Analysis Complete!")
                    st.subheader("📄 Root Cause Analysis Report")
                    st.text_area("Report", value=str(result), height=400)

                    # Save report
                    os.makedirs("output", exist_ok=True)
                    output_file = f"output/{incident_data['incident_id']}_report.txt"
                    with open(output_file, 'w') as f:
                        f.write(str(result))
                    st.info(f"💾 Report saved to: {output_file}")

                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    with col2:
        st.markdown("""
        <div class="scenario-box">
        <h3>💾 Scenario 2</h3>
        <p><strong>Memory Leak</strong></p>
        <p>UserCache memory leak causing OutOfMemory errors</p>
        <ul>
        <li>Service: user-service</li>
        <li>Severity: P1</li>
        <li>Impact: 5000 users</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔍 Analyze Scenario 2", key="s2"):
            with st.spinner("🤖 AI Agents analyzing incident..."):
                try:
                    with open("test_data/incidents/scenario2.json", 'r') as f:
                        incident_data = json.load(f)

                    crew = build_incident_response_crew(incident_data)
                    result = crew.kickoff()

                    st.success("✅ Analysis Complete!")
                    st.subheader("📄 Root Cause Analysis Report")
                    st.text_area("Report", value=str(result), height=400, key="s2_result")

                    os.makedirs("output", exist_ok=True)
                    output_file = f"output/{incident_data['incident_id']}_report.txt"
                    with open(output_file, 'w') as f:
                        f.write(str(result))
                    st.info(f"💾 Report saved to: {output_file}")

                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

    with col3:
        st.markdown("""
        <div class="scenario-box">
        <h3>🐛 Scenario 3</h3>
        <p><strong>Application Bug</strong></p>
        <p>NullPointerException causing orders to fail</p>
        <ul>
        <li>Service: order-service</li>
        <li>Severity: P2</li>
        <li>Impact: 300 users</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔍 Analyze Scenario 3", key="s3"):
            with st.spinner("🤖 AI Agents analyzing incident..."):
                try:
                    with open("test_data/incidents/scenario3.json", 'r') as f:
                        incident_data = json.load(f)

                    crew = build_incident_response_crew(incident_data)
                    result = crew.kickoff()

                    st.success("✅ Analysis Complete!")
                    st.subheader("📄 Root Cause Analysis Report")
                    st.text_area("Report", value=str(result), height=400, key="s3_result")

                    os.makedirs("output", exist_ok=True)
                    output_file = f"output/{incident_data['incident_id']}_report.txt"
                    with open(output_file, 'w') as f:
                        f.write(str(result))
                    st.info(f"💾 Report saved to: {output_file}")

                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")

with tab2:
    st.header("Create Custom Incident Analysis")
    st.write("Enter your incident details for AI-powered RCA")

    col1, col2 = st.columns(2)

    with col1:
        incident_id = st.text_input("Incident ID", "INC-2026-CUSTOM-001")
        service_name = st.text_input("Service Name", "payment-api")
        environment = st.selectbox("Environment", ["production", "staging", "development"])

    with col2:
        start_time = st.text_input("Start Time (ISO format)", "2026-03-28T10:00:00Z")
        end_time = st.text_input("End Time (ISO format)", "2026-03-28T10:30:00Z")
        affected_users = st.number_input("Affected Users", min_value=0, value=100)

    description = st.text_area("Incident Description",
                                "Payment processing failures reported by users")

    if st.button("🚀 Analyze Custom Incident", type="primary"):
        if not all([incident_id, service_name, start_time, end_time]):
            st.error("⚠️ Please fill in all required fields")
        else:
            with st.spinner("🤖 AI Agents analyzing your incident..."):
                try:
                    custom_incident = {
                        "incident_id": incident_id,
                        "service_name": service_name,
                        "environment": environment,
                        "incident_start": start_time,
                        "incident_end": end_time,
                        "initial_report": description,
                        "affected_users": affected_users
                    }

                    crew = build_incident_response_crew(custom_incident)
                    result = crew.kickoff()

                    st.success("✅ Analysis Complete!")
                    st.subheader("📄 Root Cause Analysis Report")
                    st.text_area("Report", value=str(result), height=400, key="custom_result")

                    os.makedirs("output", exist_ok=True)
                    output_file = f"output/{incident_id}_report.txt"
                    with open(output_file, 'w') as f:
                        f.write(str(result))
                    st.info(f"💾 Report saved to: {output_file}")

                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.exception(e)

with tab3:
    st.header("About Incident Response AI")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 How It Works")
        st.markdown("""
        1. **Log Analysis** - AI agent extracts errors and patterns from logs
        2. **Triage** - Assesses severity (P0-P4) and business impact
        3. **Deployment Check** - Correlates with recent deployments
        4. **Playbook Search** - Finds relevant runbooks
        5. **RCA Generation** - Synthesizes findings using 5 Whys methodology
        """)

        st.subheader("📊 Output")
        st.markdown("""
        - Executive Summary
        - Complete Timeline
        - Root Cause (5 Whys)
        - Evidence & Data
        - Remediation Steps
        - Prevention Recommendations
        """)

    with col2:
        st.subheader("🤖 AI Agents")
        st.markdown("""
        **Log Analyzer**
        - Parses application logs
        - Identifies error patterns
        - Builds incident timeline

        **Triage Specialist**
        - Classifies severity
        - Estimates impact
        - Determines escalation

        **Deployment Checker**
        - Checks deployment history
        - Analyzes code changes
        - Calculates correlation

        **RCA Expert**
        - Applies 5 Whys
        - Generates recommendations
        - Creates final report
        """)

    st.divider()

    st.subheader("📚 Test Scenarios")
    st.markdown("""
    | Scenario | Type | Root Cause | Correlation |
    |----------|------|------------|-------------|
    | 1 | Deployment | Timeout config changed | HIGH |
    | 2 | Infrastructure | Memory leak in cache | LOW |
    | 3 | Application | NullPointerException | LOW |
    """)

    st.divider()

    st.info("💡 **Tip:** Start with a pre-loaded scenario to see the system in action!")

# Footer
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Agents", "4", help="Log Analyzer, Triage, Deployment, RCA")

with col2:
    st.metric("Tasks", "5", help="Sequential AI task execution")

with col3:
    st.metric("Test Scenarios", "3", help="Ready-to-use examples")

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>Built with CrewAI | Multi-Agent Incident Response System</p>
    <p>📧 For support, check the README.md</p>
</div>
""", unsafe_allow_html=True)
