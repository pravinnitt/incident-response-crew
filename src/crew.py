from crewai import Crew, Process

from src.agents.log_analyzer import get_log_analyzer
from src.agents.triage_agent import get_triage_agent
from src.agents.deployment_checker import get_deployment_checker
from src.agents.rca_agent import get_rca_agent

from src.tasks.log_analysis_task import create_log_analysis_task
from src.tasks.triage_task import create_triage_task
from src.tasks.deployment_task import create_deployment_task
from src.tasks.playbook_task import create_playbook_task
from src.tasks.rca_task import create_rca_task


def build_incident_response_crew(incident_data: dict):
    """
    Build the incident response crew with all agents and tasks.

    Args:
        incident_data: Dictionary containing incident details

    Returns:
        Configured Crew instance
    """
    # Initialize agents
    log_analyzer = get_log_analyzer()
    triage_agent = get_triage_agent()
    deployment_checker = get_deployment_checker()
    rca_agent = get_rca_agent()

    # Create tasks with incident data
    log_task = create_log_analysis_task(log_analyzer, incident_data)
    triage_task = create_triage_task(triage_agent, incident_data)
    deployment_task = create_deployment_task(deployment_checker, incident_data)
    playbook_task = create_playbook_task(triage_agent, incident_data)
    rca_task = create_rca_task(rca_agent, incident_data)

    # Set task dependencies (context passing)
    triage_task.context = [log_task]
    deployment_task.context = [triage_task]
    playbook_task.context = [triage_task, log_task]
    rca_task.context = [log_task, triage_task, deployment_task, playbook_task]

    # Build crew
    crew = Crew(
        agents=[log_analyzer, triage_agent, deployment_checker, rca_agent],
        tasks=[log_task, triage_task, deployment_task, playbook_task, rca_task],
        process=Process.sequential,
        verbose=True,
        memory=False,  # Set to True if you want memory across runs
    )

    return crew
