from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import json
from datetime import datetime, timedelta


class DeploymentHistoryInput(BaseModel):
    """Input schema for DeploymentHistoryTool."""
    service_name: str = Field(..., description="Name of the service (e.g., 'payment-api')")
    hours_back: int = Field(default=48, description="How many hours back to look for deployments")


class DeploymentHistoryTool(BaseTool):
    name: str = "Deployment History"
    description: str = (
        "Retrieves deployment history for the service including commit info, "
        "deployment time, and deployment status."
    )
    args_schema: Type[BaseModel] = DeploymentHistoryInput

    def _run(self, service_name: str, hours_back: int = 48) -> str:
        """Execute the deployment history tool."""
        # Map service names to deployment files
        deployment_file_map = {
            "payment-api": "test_data/deployments/payment-api.json",
            "user-service": "test_data/deployments/user-service.json",
            "order-service": "test_data/deployments/order-service.json",
        }

        deployment_file = deployment_file_map.get(service_name)

        if not deployment_file or not os.path.exists(deployment_file):
            return f"Error: Deployment history not found for service '{service_name}'"

        try:
            with open(deployment_file, 'r') as f:
                data = json.load(f)

            result = f"=== Deployment History for {service_name} (Last {hours_back} hours) ===\n\n"

            for deploy in data.get("deployments", []):
                result += f"Deployment ID: {deploy['id']}\n"
                result += f"Version: {deploy['version']}\n"
                result += f"Timestamp: {deploy['timestamp']}\n"
                result += f"Status: {deploy['status']}\n"
                result += f"Author: {deploy['author']}\n"
                result += f"Commit: {deploy['commit']}\n"

                if "changes" in deploy:
                    result += "Changes:\n"
                    for change in deploy['changes']:
                        result += f"  - {change}\n"

                if deploy.get('status') == 'rolled_back' and 'rollback_time' in deploy:
                    result += f"⚠️ ROLLBACK at {deploy['rollback_time']}\n"

                result += "\n" + "-" * 60 + "\n\n"

            return result

        except Exception as e:
            return f"Error reading deployment history: {str(e)}"


class GitDiffInput(BaseModel):
    """Input schema for GitDiffTool."""
    service_name: str = Field(..., description="Name of the service")
    from_version: str = Field(..., description="Previous version")
    to_version: str = Field(..., description="Current version")


class GitDiffTool(BaseTool):
    name: str = "Git Diff Analyzer"
    description: str = (
        "Analyzes git differences between versions to identify potentially "
        "problematic changes."
    )
    args_schema: Type[BaseModel] = GitDiffInput

    def _run(self, service_name: str, from_version: str, to_version: str) -> str:
        """Execute the git diff analyzer tool."""
        # Simplified git diff analysis based on deployment data
        deployment_file_map = {
            "payment-api": "test_data/deployments/payment-api.json",
            "user-service": "test_data/deployments/user-service.json",
            "order-service": "test_data/deployments/order-service.json",
        }

        deployment_file = deployment_file_map.get(service_name)

        if not deployment_file or not os.path.exists(deployment_file):
            return f"No git diff data available for {service_name}"

        try:
            with open(deployment_file, 'r') as f:
                data = json.load(f)

            result = f"=== Git Diff Analysis: {from_version} -> {to_version} ===\n\n"

            # Find the deployment
            for deploy in data.get("deployments", []):
                if deploy['version'] == to_version:
                    result += f"Commit: {deploy['commit']}\n"
                    result += f"Author: {deploy['author']}\n\n"

                    if "changes" in deploy:
                        result += "Code Changes:\n"
                        for change in deploy['changes']:
                            result += f"  • {change}\n"

                            # Flag suspicious changes
                            if "timeout" in change.lower():
                                result += "    ⚠️ SUSPICIOUS: Timeout configuration changed\n"
                            if "pool" in change.lower():
                                result += "    ⚠️ SUSPICIOUS: Connection pool modified\n"
                            if "retry" in change.lower():
                                result += "    ⚠️ SUSPICIOUS: Retry logic changed\n"
                            if "cache" in change.lower():
                                result += "    ⚠️ SUSPICIOUS: Cache configuration changed\n"

                    break

            return result

        except Exception as e:
            return f"Error analyzing git diff: {str(e)}"


# Create instances of the tools
deployment_history_tool = DeploymentHistoryTool()
git_diff_tool = GitDiffTool()
