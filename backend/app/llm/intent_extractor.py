from backend.app.llm.provider import LLMProvider
from backend.app.schemas.intent import ShoppingIntent


class IntentExtractor:

    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def extract(self, user_message: str) -> ShoppingIntent:
        result = self.provider.extract_intent(user_message)

        if not isinstance(result, ShoppingIntent):
            raise TypeError(
                "LLM provider returned an invalid intent."
            )

        return result