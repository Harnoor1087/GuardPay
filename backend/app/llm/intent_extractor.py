from backend.app.llm.exceptions import LLMProviderError
from backend.app.llm.provider import LLMProvider
from backend.app.schemas.intent import ShoppingIntent


class IntentExtractor:

    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def extract(self, user_message: str) -> ShoppingIntent:

        try:
            result = self.provider.extract_intent(
                user_message
            )

        except Exception as exc:
            raise LLMProviderError() from exc

        if not isinstance(result, ShoppingIntent):
            raise TypeError(
                "LLM provider returned an invalid intent."
            )

        return result