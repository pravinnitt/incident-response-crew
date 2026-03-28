#!/usr/bin/env python3
"""
Simple test to verify all files exist and structure is correct.
This test does NOT require dependencies installed.
"""

import os
import sys

def test_file_exists(filepath, description):
    """Test if a file exists"""
    if os.path.exists(filepath):
        print(f"✓ {description}")
        return True
    else:
        print(f"✗ MISSING: {description} - {filepath}")
        return False

def main():
    print("\n" + "="*60)
    print("Incident Response System - Structure Verification")
    print("="*60 + "\n")

    all_passed = True

    # Core files
    print("📄 Core Application Files:")
    all_passed &= test_file_exists("main.py", "main.py")
    all_passed &= test_file_exists("pyproject.toml", "pyproject.toml")
    all_passed &= test_file_exists("README.md", "README.md")
    all_passed &= test_file_exists("QUICKSTART.md", "QUICKSTART.md")
    all_passed &= test_file_exists(".env.example", ".env.example")
    all_passed &= test_file_exists(".gitignore", ".gitignore")
    print()

    # Agent files
    print("🤖 Agent Files:")
    all_passed &= test_file_exists("src/agents/log_analyzer.py", "Log Analyzer Agent")
    all_passed &= test_file_exists("src/agents/triage_agent.py", "Triage Agent")
    all_passed &= test_file_exists("src/agents/deployment_checker.py", "Deployment Checker Agent")
    all_passed &= test_file_exists("src/agents/rca_agent.py", "RCA Agent")
    print()

    # Task files
    print("📋 Task Files:")
    all_passed &= test_file_exists("src/tasks/log_analysis_task.py", "Log Analysis Task")
    all_passed &= test_file_exists("src/tasks/triage_task.py", "Triage Task")
    all_passed &= test_file_exists("src/tasks/deployment_task.py", "Deployment Task")
    all_passed &= test_file_exists("src/tasks/playbook_task.py", "Playbook Task")
    all_passed &= test_file_exists("src/tasks/rca_task.py", "RCA Task")
    print()

    # Tool files
    print("🛠️  Tool Files:")
    all_passed &= test_file_exists("src/tools/log_tools.py", "Log Tools")
    all_passed &= test_file_exists("src/tools/deployment_tools.py", "Deployment Tools")
    all_passed &= test_file_exists("src/tools/playbook_tools.py", "Playbook Tools")
    print()

    # Config files
    print("⚙️  Configuration Files:")
    all_passed &= test_file_exists("src/config.py", "LLM Config")
    all_passed &= test_file_exists("src/crew.py", "Crew Orchestration")
    print()

    # Log files
    print("📝 Test Log Files:")
    all_passed &= test_file_exists("test_data/logs/payment-api-scenario1.log", "Payment API Logs")
    all_passed &= test_file_exists("test_data/logs/user-service-scenario2.log", "User Service Logs")
    all_passed &= test_file_exists("test_data/logs/order-service-scenario3.log", "Order Service Logs")
    print()

    # Deployment files
    print("🚀 Deployment History Files:")
    all_passed &= test_file_exists("test_data/deployments/payment-api.json", "Payment API Deployments")
    all_passed &= test_file_exists("test_data/deployments/user-service.json", "User Service Deployments")
    all_passed &= test_file_exists("test_data/deployments/order-service.json", "Order Service Deployments")
    print()

    # Playbook files
    print("📖 Playbook Files:")
    all_passed &= test_file_exists("test_data/playbooks/database-timeout.md", "Database Timeout Playbook")
    all_passed &= test_file_exists("test_data/playbooks/memory-leak.md", "Memory Leak Playbook")
    all_passed &= test_file_exists("test_data/playbooks/null-pointer-exception.md", "NPE Playbook")
    print()

    # Scenario files
    print("🎯 Test Scenario Files:")
    all_passed &= test_file_exists("test_data/incidents/scenario1.json", "Scenario 1")
    all_passed &= test_file_exists("test_data/incidents/scenario2.json", "Scenario 2")
    all_passed &= test_file_exists("test_data/incidents/scenario3.json", "Scenario 3")
    print()

    # Test scripts
    print("🏃 Quick Test Scripts:")
    all_passed &= test_file_exists("run_scenario1.sh", "Scenario 1 Script")
    all_passed &= test_file_exists("run_scenario2.sh", "Scenario 2 Script")
    all_passed &= test_file_exists("run_scenario3.sh", "Scenario 3 Script")
    print()

    # Check file contents (sample)
    print("🔍 Verifying File Contents:")

    # Check main.py has required imports
    with open("main.py", 'r') as f:
        main_content = f.read()
        if "from src.crew import build_incident_response_crew" in main_content:
            print("✓ main.py has correct imports")
        else:
            print("✗ main.py missing imports")
            all_passed = False

    # Check log file has content
    with open("test_data/logs/payment-api-scenario1.log", 'r') as f:
        log_content = f.read()
        if "[ERROR]" in log_content and "timeout" in log_content.lower():
            print("✓ Log files have realistic content")
        else:
            print("✗ Log files missing expected content")
            all_passed = False

    # Check JSON scenario
    import json
    with open("test_data/incidents/scenario1.json", 'r') as f:
        scenario = json.load(f)
        if "incident_id" in scenario and "service_name" in scenario:
            print("✓ Scenario files have correct structure")
        else:
            print("✗ Scenario files missing required fields")
            all_passed = False

    print()
    print("="*60)

    if all_passed:
        print("🎉 ALL STRUCTURE TESTS PASSED!")
        print("="*60)
        print("\n✅ File structure is complete and correct!")
        print("\n📋 Next Steps:")
        print("  1. Install dependencies:")
        print("     pip install crewai litellm openai python-dotenv")
        print()
        print("  2. Configure API key:")
        print("     cp .env.example .env")
        print("     # Add GROQ_API_KEY=your_key to .env")
        print()
        print("  3. Run a test scenario:")
        print("     python3 main.py --scenario 1")
        print()
    else:
        print("❌ SOME TESTS FAILED")
        print("="*60)
        sys.exit(1)

if __name__ == "__main__":
    main()
