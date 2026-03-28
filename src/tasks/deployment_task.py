from crewai import Task


def create_deployment_task(agent, incident_data):
    return Task(
        description=f"""
        Check for recent deployments or configuration changes that may have caused the incident.

        Incident Details:
        - Service: {incident_data['service_name']}
        - Incident Start Time: {incident_data['incident_start']}

        Your tasks:
        1. Use the Deployment History tool to fetch recent deployments (last 48 hours)
        2. Calculate time between deployments and incident start time
        3. Use Git Diff Analyzer tool to analyze code changes in recent deployments
        4. Identify suspicious changes:
           - Configuration changes (timeouts, connection pools, caches)
           - Logic changes in critical paths
           - Dependency updates
           - Infrastructure changes

        5. Determine correlation confidence:
           - HIGH: Incident within 2 hours of deployment + suspicious changes
           - MEDIUM: Incident within 24 hours of deployment
           - LOW: No recent deployments or no suspicious changes

        6. Assess rollback status (was a rollback performed?)
        7. Recommend rollback if correlation is HIGH and not yet rolled back

        Correlation Rules:
        - Incident within 5 minutes of deployment: Very suspicious
        - Incident within 1 hour of deployment: Highly suspicious
        - Incident within 24 hours: Moderately suspicious
        - Incident after 48+ hours: Likely not deployment-related

        Be thorough in analyzing the timeline and changes.
        """,
        agent=agent,
        expected_output="""Deployment Correlation Report containing:
        - Correlation Confidence Score (HIGH/MEDIUM/LOW) with reasoning
        - Recent Deployment List (last 48 hours) with timestamps
        - Time Between Deployment and Incident (in minutes)
        - Code Changes Analysis (list of changes with risk assessment)
        - Suspicious Changes Identified (flagged items)
        - Rollback Status (performed? when? effective?)
        - Rollback Recommendation (if applicable)
        - Configuration Changes Impact Assessment""",
    )
