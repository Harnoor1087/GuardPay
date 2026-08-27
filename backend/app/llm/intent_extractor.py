from backend.app.llm.provider import LLMProvider
from backend.app.schemas.intent import ShoppingIntent


class IntentExtractor:

    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def extract(self, user_message: str) -> ShoppingIntent:
        return self.provider.extract_intent(user_message)