import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()


def get_llm():
    """Return LLM based on available environment"""

    # Priority 1: Groq (Fast and Free)
    if os.getenv("GROQ_API_KEY"):
        return LLM(
            model="groq/llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY")
        )

    # Priority 2: OpenAI
    elif os.getenv("OPENAI_API_KEY"):
        return LLM(
            model="gpt-4o-mini",
            temperature=0.2
        )

    # Priority 3: Ollama (local only - won't work on cloud)
    else:
        return LLM(
            model="ollama/llama3:8b",
            base_url="http://localhost:11434",
            temperature=0.2
        )
