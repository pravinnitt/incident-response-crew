from crewai import Task


def create_playbook_task(agent, incident_data):
    return Task(
        description=f"""
        Search for and retrieve relevant runbooks/playbooks based on the incident classification
        and error patterns identified.

        Your tasks:
        1. Review the triage results to understand the incident category
        2. Review the log analysis to identify error keywords
        3. Use the Playbook Search tool with:
           - Incident type from triage (e.g., 'database', 'memory', 'application')
           - Error keywords from logs (e.g., 'timeout', 'OutOfMemory', 'NullPointer')

        4. Extract relevant sections from matched playbooks:
           - Symptoms matching our incident
           - Common causes
           - Troubleshooting steps
           - Resolution procedures
           - Prevention measures

        5. Map playbook recommendations to current incident findings
        6. Highlight steps already taken vs steps still needed

        Focus on actionable guidance that applies to this specific incident.
        """,
        agent=agent,
        expected_output="""Playbook Consultation Report containing:
        - List of Applicable Playbooks (titles and relevance scores)
        - Matched Symptoms (from playbooks that match our incident)
        - Common Causes (from playbooks)
        - Recommended Troubleshooting Steps (prioritized)
        - Resolution Procedures (from playbooks)
        - Prevention Measures (from playbooks)
        - Mapping to Current Incident (which steps apply, which are already done)""",
    )
