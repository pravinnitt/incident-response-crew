import os
from dotenv import load_dotenv
from crewai import LLM
from src.rate_limiter import groq_rate_limiter

load_dotenv()


def get_llm(use_rate_limiter=True):
    """
    Return LLM based on available environment.

    Args:
        use_rate_limiter: Whether to apply rate limiting for Groq API
    """

    # Priority 1: Groq (Fast and Free)
    if os.getenv("GROQ_API_KEY"):
        # Apply rate limiting before making requests
        if use_rate_limiter:
            groq_rate_limiter.wait_if_needed(estimated_tokens=800)

        return LLM(
            model="groq/llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY"),
            temperature=0.3,  # Slightly higher for more concise responses
            max_tokens=500  # Limit response length to conserve tokens
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
