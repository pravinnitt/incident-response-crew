from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os


class PlaybookSearchInput(BaseModel):
    """Input schema for PlaybookSearchTool."""
    incident_type: str = Field(..., description="Type of incident (e.g., 'database', 'memory', 'application')")
    error_keywords: str = Field(..., description="Keywords from errors (e.g., 'timeout', 'OutOfMemory', 'NullPointer')")


class PlaybookSearchTool(BaseTool):
    name: str = "Playbook Search"
    description: str = (
        "Searches knowledge base for relevant playbooks and runbooks "
        "based on incident type and error patterns. "
        "Returns relevant playbook content and recommendations."
    )
    args_schema: Type[BaseModel] = PlaybookSearchInput

    def _run(self, incident_type: str, error_keywords: str) -> str:
        """Execute the playbook search tool."""
        playbook_dir = "test_data/playbooks"

        if not os.path.exists(playbook_dir):
            return "No playbooks available"

        # Map keywords to playbook files
        keyword_map = {
            "timeout": "database-timeout.md",
            "database": "database-timeout.md",
            "connection": "database-timeout.md",
            "memory": "memory-leak.md",
            "outofmemory": "memory-leak.md",
            "heap": "memory-leak.md",
            "nullpointer": "null-pointer-exception.md",
            "null": "null-pointer-exception.md",
            "npe": "null-pointer-exception.md",
        }

        # Find matching playbooks
        keywords_lower = error_keywords.lower() if error_keywords else ""
        matching_playbooks = set()

        for keyword, playbook in keyword_map.items():
            if keyword in keywords_lower or keyword in incident_type.lower():
                matching_playbooks.add(playbook)

        if not matching_playbooks:
            return "No matching playbooks found for the given incident type and keywords"

        result = "=== Applicable Playbooks ===\n\n"

        for playbook_file in matching_playbooks:
            playbook_path = os.path.join(playbook_dir, playbook_file)

            if os.path.exists(playbook_path):
                with open(playbook_path, 'r') as f:
                    content = f.read()

                result += f"📖 Playbook: {playbook_file}\n"
                result += "=" * 60 + "\n"
                result += content
                result += "\n\n"

        return result


# Create instance of the tool
playbook_search_tool = PlaybookSearchTool()
