from crewai import Task


def create_log_analysis_task(agent, incident_data):
    return Task(
        description=f"""
        Analyze logs from the incident timeframe for service {incident_data['service_name']}.

        Incident Details:
        - Service: {incident_data['service_name']}
        - Environment: {incident_data['environment']}
        - Time Range: {incident_data['incident_start']} to {incident_data['incident_end']}
        - Initial Report: {incident_data.get('initial_report', 'N/A')}

        Your tasks:
        1. Use the Log Reader tool to fetch logs for the service and time range
        2. Use the Pattern Matcher tool to analyze the logs for patterns
        3. Identify all ERROR and WARN level messages
        4. Extract stack traces and error codes
        5. Determine the frequency of different error types
        6. Identify any anomalies (sudden spikes, unusual patterns)
        7. Create a timeline of significant log events

        Focus on:
        - Critical errors and exceptions
        - Warning patterns before the incident
        - Unusual log volume or frequency changes
        - Failed requests, timeouts, or connection errors
        - Resource exhaustion indicators (memory, CPU, connections)

        Provide a clear, structured analysis with exact error counts and timestamps.
        """,
        agent=agent,
        expected_output="""A structured report containing:
        - Timeline of critical errors with exact timestamps
        - All unique error messages with frequencies
        - Pattern anomalies (frequency spikes, unusual patterns)
        - Affected components and services
        - Error codes and stack traces
        - Assessment of log patterns (what do the logs tell us?)""",
    )
