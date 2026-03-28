import argparse
import json
from src.crew import build_incident_response_crew
import os
from dotenv import load_dotenv

load_dotenv()


def load_scenario(scenario_num):
    """Load a predefined test scenario"""
    scenario_path = f"test_data/incidents/scenario{scenario_num}.json"
    if os.path.exists(scenario_path):
        with open(scenario_path, 'r') as f:
            return json.load(f)
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Incident Response AI System using CrewAI"
    )
    parser.add_argument(
        "--scenario",
        type=int,
        help="Load predefined test scenario (1, 2, or 3)",
    )
    parser.add_argument(
        "--incident-id",
        type=str,
        help="Incident ID",
    )
    parser.add_argument(
        "--service",
        type=str,
        help="Service name (e.g., payment-api)",
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="production",
        help="Environment (production, staging, etc.)",
    )
    parser.add_argument(
        "--start-time",
        type=str,
        help="Incident start time (ISO format)",
    )
    parser.add_argument(
        "--end-time",
        type=str,
        help="Incident end time (ISO format)",
    )
    parser.add_argument(
        "--description",
        type=str,
        help="Incident description",
    )

    args = parser.parse_args()

    # Load scenario if specified
    if args.scenario:
        print(f"\n{'='*80}")
        print(f"Loading Test Scenario {args.scenario}...")
        print(f"{'='*80}\n")
        incident_data = load_scenario(args.scenario)
        if not incident_data:
            print(f"Error: Scenario {args.scenario} not found!")
            return
    else:
        # Build incident data from arguments
        if not all([args.incident_id, args.service, args.start_time, args.end_time]):
            print("Error: Required arguments missing!")
            print("Use --scenario [1-3] for test scenarios or provide:")
            print("  --incident-id --service --start-time --end-time")
            return

        incident_data = {
            "incident_id": args.incident_id,
            "service_name": args.service,
            "environment": args.environment,
            "incident_start": args.start_time,
            "incident_end": args.end_time,
            "initial_report": args.description or "No description provided",
        }

    print(f"\n{'='*80}")
    print(f"INCIDENT RESPONSE SYSTEM - ANALYSIS STARTED")
    print(f"{'='*80}")
    print(f"Incident ID: {incident_data['incident_id']}")
    print(f"Service: {incident_data['service_name']}")
    print(f"Environment: {incident_data['environment']}")
    print(f"Time Range: {incident_data['incident_start']} to {incident_data['incident_end']}")
    print(f"{'='*80}\n")

    # Build and execute crew
    crew = build_incident_response_crew(incident_data)
    result = crew.kickoff()

    print(f"\n{'='*80}")
    print(f"INCIDENT RESPONSE ANALYSIS COMPLETE")
    print(f"{'='*80}\n")
    print(result)

    # Save output
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_file = f"{output_dir}/{incident_data['incident_id']}_report.txt"
    with open(output_file, 'w') as f:
        f.write(str(result))
    print(f"\n✅ Report saved to: {output_file}\n")


if __name__ == "__main__":
    main()
