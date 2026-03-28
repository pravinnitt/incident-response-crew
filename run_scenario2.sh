#!/bin/bash

# Quick test script for Scenario 2: Infrastructure Incident

echo "=========================================="
echo "Running Scenario 2: Memory Leak"
echo "=========================================="
echo ""
echo "Description: Memory leak causing OutOfMemory"
echo "Expected: LOW deployment correlation"
echo ""

python main.py --scenario 2
