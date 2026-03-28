"""Rate limiter for API calls to stay within free tier limits."""
import time
import threading
from collections import deque
from datetime import datetime, timedelta


class RateLimiter:
    """Token-based rate limiter for Groq API calls."""

    def __init__(self, tokens_per_minute=5000, buffer=1000):
        """
        Initialize rate limiter.

        Args:
            tokens_per_minute: Max tokens per minute (default 5000, leaving buffer from 6000 limit)
            buffer: Safety buffer to prevent hitting exact limit
        """
        self.max_tokens = tokens_per_minute
        self.buffer = buffer
        self.requests = deque()
        self.lock = threading.Lock()
        self.total_tokens_used = 0

    def wait_if_needed(self, estimated_tokens=500):
        """
        Wait if necessary to stay within rate limits.

        Args:
            estimated_tokens: Estimated tokens for this request
        """
        with self.lock:
            now = datetime.now()
            one_minute_ago = now - timedelta(minutes=1)

            # Remove requests older than 1 minute
            while self.requests and self.requests[0]['timestamp'] < one_minute_ago:
                old_request = self.requests.popleft()
                self.total_tokens_used -= old_request['tokens']

            # Check if we need to wait
            if self.total_tokens_used + estimated_tokens > self.max_tokens:
                if self.requests:
                    # Calculate wait time until oldest request expires
                    oldest_request = self.requests[0]['timestamp']
                    wait_time = 60 - (now - oldest_request).total_seconds()

                    if wait_time > 0:
                        print(f"⏳ Rate limit approaching. Waiting {wait_time:.1f}s...")
                        time.sleep(wait_time + 1)  # Add 1s buffer

                        # Recursively check again after waiting
                        return self.wait_if_needed(estimated_tokens)

            # Record this request
            self.requests.append({
                'timestamp': now,
                'tokens': estimated_tokens
            })
            self.total_tokens_used += estimated_tokens

    def get_current_usage(self):
        """Get current token usage in the last minute."""
        with self.lock:
            now = datetime.now()
            one_minute_ago = now - timedelta(minutes=1)

            # Clean old requests
            while self.requests and self.requests[0]['timestamp'] < one_minute_ago:
                old_request = self.requests.popleft()
                self.total_tokens_used -= old_request['tokens']

            return {
                'tokens_used': self.total_tokens_used,
                'tokens_limit': self.max_tokens,
                'tokens_available': self.max_tokens - self.total_tokens_used
            }


# Global rate limiter instance
groq_rate_limiter = RateLimiter(tokens_per_minute=5000)
