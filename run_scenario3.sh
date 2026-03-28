#!/bin/bash

# Quick test script for Scenario 3: Application Bug

echo "=========================================="
echo "Running Scenario 3: Application Bug"
echo "=========================================="
echo ""
echo "Description: NullPointerException in order processing"
echo "Expected: LOW deployment correlation, code bug"
echo ""

python main.py --scenario 3
