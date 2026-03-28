"""
Test script to verify the incident response system
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.agents.log_analyzer import get_log_analyzer
from src.agents.triage_agent import get_triage_agent
from src.agents.deployment_checker import get_deployment_checker
from src.agents.rca_agent import get_rca_agent
from src.tools.log_tools import log_reader_tool, pattern_matcher_tool
from src.tools.deployment_tools import deployment_history_tool
from src.tools.playbook_tools import playbook_search_tool


def test_agents():
    """Test that all agents can be created"""
    print("Testing agent creation...")

    log_agent = get_log_analyzer()
    assert log_agent is not None
    assert log_agent.role == "Log Analysis Expert"
    print("✓ Log Analyzer created")

    triage_agent = get_triage_agent()
    assert triage_agent is not None
    assert triage_agent.role == "Incident Triage Specialist"
    print("✓ Triage Agent created")

    deploy_agent = get_deployment_checker()
    assert deploy_agent is not None
    assert deploy_agent.role == "Deployment Correlation Analyst"
    print("✓ Deployment Checker created")

    rca_agent = get_rca_agent()
    assert rca_agent is not None
    assert rca_agent.role == "Root Cause Analysis Expert"
    print("✓ RCA Agent created")

    print("\n✅ All agents created successfully\n")


def test_tools():
    """Test that all tools work"""
    print("Testing tools...")

    # Test log reader
    result = log_reader_tool("payment-api", "2026-03-28T10:00:00Z", "2026-03-28T10:30:00Z")
    assert "payment-api" in result
    print("✓ Log Reader tool works")

    # Test pattern matcher
    sample_logs = "[ERROR] test error\n[ERROR] test error\n[WARN] warning"
    result = pattern_matcher_tool(sample_logs)
    assert "ERRORS" in result
    print("✓ Pattern Matcher tool works")

    # Test deployment history
    result = deployment_history_tool("payment-api", 48)
    assert "payment-api" in result
    print("✓ Deployment History tool works")

    # Test playbook search
    result = playbook_search_tool("database", "timeout")
    assert "timeout" in result.lower() or "Playbook" in result
    print("✓ Playbook Search tool works")

    print("\n✅ All tools working\n")


def test_test_data():
    """Test that all test data files exist"""
    print("Testing test data files...")

    # Check log files
    log_files = [
        "test_data/logs/payment-api-scenario1.log",
        "test_data/logs/user-service-scenario2.log",
        "test_data/logs/order-service-scenario3.log"
    ]

    for log_file in log_files:
        assert os.path.exists(log_file), f"Missing: {log_file}"
        print(f"✓ {log_file}")

    # Check deployment files
    deployment_files = [
        "test_data/deployments/payment-api.json",
        "test_data/deployments/user-service.json",
        "test_data/deployments/order-service.json"
    ]

    for deploy_file in deployment_files:
        assert os.path.exists(deploy_file), f"Missing: {deploy_file}"
        print(f"✓ {deploy_file}")

    # Check playbook files
    playbook_files = [
        "test_data/playbooks/database-timeout.md",
        "test_data/playbooks/memory-leak.md",
        "test_data/playbooks/null-pointer-exception.md"
    ]

    for playbook_file in playbook_files:
        assert os.path.exists(playbook_file), f"Missing: {playbook_file}"
        print(f"✓ {playbook_file}")

    # Check scenario files
    scenario_files = [
        "test_data/incidents/scenario1.json",
        "test_data/incidents/scenario2.json",
        "test_data/incidents/scenario3.json"
    ]

    for scenario_file in scenario_files:
        assert os.path.exists(scenario_file), f"Missing: {scenario_file}"
        print(f"✓ {scenario_file}")

    print("\n✅ All test data files present\n")


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("Incident Response System - Test Suite")
    print("="*60 + "\n")

    try:
        test_test_data()
        test_tools()
        test_agents()

        print("="*60)
        print("🎉 ALL TESTS PASSED!")
        print("="*60)
        print("\nYou can now run scenarios:")
        print("  python main.py --scenario 1")
        print("  python main.py --scenario 2")
        print("  python main.py --scenario 3")
        print()

    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
