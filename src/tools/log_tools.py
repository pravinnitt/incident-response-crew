from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
from datetime import datetime


class LogReaderInput(BaseModel):
    """Input schema for LogReaderTool."""
    service_name: str = Field(..., description="Name of the service (e.g., 'payment-api', 'user-service', 'order-service')")
    start_time: str = Field(..., description="Start time in ISO format")
    end_time: str = Field(..., description="End time in ISO format")


class LogReaderTool(BaseTool):
    name: str = "Log Reader"
    description: str = (
        "Reads logs from the specified service within the given time range. "
        "Returns formatted log entries with timestamps, severity levels, and messages."
    )
    args_schema: Type[BaseModel] = LogReaderInput

    def _run(self, service_name: str, start_time: str, end_time: str) -> str:
        """Execute the log reader tool."""
        # Map service names to log files
        log_file_map = {
            "payment-api": "test_data/logs/payment-api-scenario1.log",
            "user-service": "test_data/logs/user-service-scenario2.log",
            "order-service": "test_data/logs/order-service-scenario3.log",
        }

        log_file = log_file_map.get(service_name)

        if not log_file or not os.path.exists(log_file):
            return f"Error: Log file not found for service '{service_name}'"

        try:
            with open(log_file, 'r') as f:
                logs = f.read()

            return f"=== Logs for {service_name} ===\n{logs}"

        except Exception as e:
            return f"Error reading logs: {str(e)}"


class PatternMatcherInput(BaseModel):
    """Input schema for PatternMatcherTool."""
    logs: str = Field(..., description="Log content to analyze for patterns, errors, and anomalies")


class PatternMatcherTool(BaseTool):
    name: str = "Pattern Matcher"
    description: str = (
        "Analyzes log content to identify patterns, error frequencies, and anomalies. "
        "Returns analysis of error patterns, frequencies, and key findings."
    )
    args_schema: Type[BaseModel] = PatternMatcherInput

    def _run(self, logs: str) -> str:
        """Execute the pattern matcher tool."""
        if not logs or "Error" in logs[:100]:
            return "No valid logs provided for pattern matching"

        # Count error levels
        error_count = logs.count("[ERROR]")
        warn_count = logs.count("[WARN]")
        info_count = logs.count("[INFO]")

        # Extract common error patterns
        lines = logs.split('\n')
        error_lines = [line for line in lines if "[ERROR]" in line]

        # Simple pattern detection
        error_messages = {}
        for line in error_lines:
            # Extract error message (simplified)
            if ":" in line:
                parts = line.split(":", 3)
                if len(parts) >= 4:
                    msg = parts[3].strip().split("-")[0].strip()
                    error_messages[msg] = error_messages.get(msg, 0) + 1

        result = f"""
=== Log Pattern Analysis ===

Error Level Counts:
- ERRORS: {error_count}
- WARNINGS: {warn_count}
- INFO: {info_count}

Top Error Messages:
"""

        for msg, count in sorted(error_messages.items(), key=lambda x: x[1], reverse=True)[:5]:
            result += f"- {msg} (Count: {count})\n"

        # Detect anomalies
        if error_count > 50:
            result += f"\n⚠️ ANOMALY: High error count ({error_count}) detected - potential incident\n"

        if "timeout" in logs.lower():
            result += "⚠️ PATTERN: Timeout errors detected - possible connectivity issues\n"

        if "OutOfMemoryError" in logs:
            result += "⚠️ PATTERN: Memory issues detected - potential resource exhaustion\n"

        if "NullPointerException" in logs:
            result += "⚠️ PATTERN: Null pointer exceptions - possible application bug\n"

        return result


# Create instances of the tools
log_reader_tool = LogReaderTool()
pattern_matcher_tool = PatternMatcherTool()
