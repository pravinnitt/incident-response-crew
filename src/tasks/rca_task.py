from crewai import Task


def create_rca_task(agent, incident_data):
    return Task(
        description=f"""
        Synthesize ALL findings from previous analyses to determine the root cause
        and provide comprehensive recommendations.

        You have access to:
        1. Log Analysis findings (errors, patterns, timeline)
        2. Triage Assessment (severity, category, impact)
        3. Deployment Correlation (recent changes, suspicious modifications)
        4. Playbook Recommendations (known solutions, best practices)

        Your tasks:
        1. Review ALL previous task outputs carefully
        2. Create a complete timeline of events (deployment → errors → resolution)
        3. Apply the 5 Whys methodology:
           - Why did the incident occur? (symptom)
           - Why did that happen? (contributing factor)
           - Why did that happen? (proximate cause)
           - Why did that happen? (root cause)
           - Why did that happen? (systemic issue)

        4. Distinguish between:
           - Root Cause: The fundamental reason (the ONE thing that if fixed prevents recurrence)
           - Contributing Factors: Things that made it worse or allowed it to happen
           - Symptoms: Observable effects that users experienced

        5. Provide evidence for your conclusions:
           - Quote specific log entries
           - Reference deployment changes
           - Cite correlation timing
           - Use data from all previous analyses

        6. Generate recommendations in three categories:
           - Immediate Remediation: What should be done NOW
           - Short-term Prevention: Actions in next 1-2 weeks
           - Long-term Prevention: Systemic improvements over 1-3 months

        7. Include Post-Incident Actions:
           - Documentation updates needed
           - Team training requirements
           - Process improvements
           - Monitoring/alerting enhancements

        Be specific, actionable, and executive-friendly while maintaining technical accuracy.
        """,
        agent=agent,
        expected_output="""Complete Root Cause Analysis Report containing:

        1. EXECUTIVE SUMMARY
           - One clear root cause statement (1-2 sentences)
           - Severity and impact summary
           - Resolution status

        2. INCIDENT TIMELINE
           - Chronological sequence of all events
           - Key timestamps (deployment, first error, peak, resolution)

        3. LOG ANALYSIS SUMMARY
           - Key errors and frequencies
           - Pattern findings

        4. SEVERITY & IMPACT
           - Classification and user impact
           - Business impact

        5. DEPLOYMENT CORRELATION
           - Correlation confidence and evidence
           - Suspicious changes identified

        6. ROOT CAUSE ANALYSIS
           - 5 Whys breakdown (structured)
           - Root Cause statement
           - Contributing Factors list
           - Evidence supporting conclusion

        7. IMMEDIATE REMEDIATION
           - Actions already taken
           - Resolution effectiveness
           - Time to resolution

        8. PREVENTION RECOMMENDATIONS
           - Short-term actions (1-2 weeks)
           - Long-term improvements (1-3 months)
           - Post-incident action items

        9. LESSONS LEARNED
           - What worked well
           - What could be improved
           - Process gaps identified

        Format as a clear, professional incident report suitable for management review.""",
    )
