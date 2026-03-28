#!/bin/bash

# Quick test script for Scenario 1: Deployment-Related Incident

echo "=========================================="
echo "Running Scenario 1: Deployment Issue"
echo "=========================================="
echo ""
echo "Description: Database timeout configuration changed"
echo "Expected: HIGH deployment correlation"
echo ""

python main.py --scenario 1
