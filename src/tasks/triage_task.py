from crewai import Task


def create_triage_task(agent, incident_data):
    return Task(
        description=f"""
        Based on the log analysis results, assess the incident and classify it.

        Incident Details:
        - Incident ID: {incident_data['incident_id']}
        - Service: {incident_data['service_name']}
        - Environment: {incident_data['environment']}

        Your tasks:
        1. Review the log analysis findings from the previous task
        2. Determine the severity level using this classification:
           - P0 (Critical): Complete service outage, all users affected, revenue impact
           - P1 (High): Major functionality broken, large user impact, significant revenue impact
           - P2 (Medium): Important feature degraded, moderate user impact
           - P3 (Low): Minor issue, small user impact, workaround available
           - P4 (Informational): No user impact, logging/monitoring issue

        3. Categorize the incident type:
           - Application (code bugs, logic errors)
           - Infrastructure (CPU, memory, disk, network)
           - Database (connection, query performance, corruption)
           - Deployment (recent changes causing issues)
           - External Dependency (third-party service failure)
           - Security (breaches, attacks)

        4. Estimate user impact (number of users, affected regions, services)
        5. Assess business impact (revenue, reputation, SLA breach risk)
        6. Determine if escalation is needed
        7. Provide immediate recommended actions

        Be specific and data-driven in your assessment.
        """,
        agent=agent,
        expected_output="""Incident Classification Report containing:
        - Severity Level (P0/P1/P2/P3/P4) with clear reasoning
        - Incident Category (Application/Infrastructure/Database/etc.)
        - User Impact Assessment (number of users, affected functionality)
        - Business Impact Assessment (revenue, SLA, reputation)
        - Affected Services/Components (list)
        - Escalation Recommendation (yes/no with reasoning)
        - Immediate Recommended Actions (prioritized list)""",
    )
