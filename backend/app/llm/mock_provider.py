from backend.app.llm.provider import LLMProvider
from backend.app.schemas.intent import ShoppingIntent


class MockLLMProvider(LLMProvider):

    def extract_intent(self, user_message: str) -> ShoppingIntent:
        """
        Temporary deterministic provider used during development
        when a real LLM API is unavailable.
        """

        message = user_message.lower()

        return ShoppingIntent(
            category="running_shoes" if "running" in message else None,
            max_price=5000 if "5000" in message else None,
            brand="Nike" if "nike" in message else None,
            use_case="road_running" if "road" in message else None,
        )