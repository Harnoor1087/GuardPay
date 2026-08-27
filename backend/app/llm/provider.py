from abc import ABC, abstractmethod

from backend.app.schemas.intent import ShoppingIntent


class LLMProvider(ABC):

    @abstractmethod
    def extract_intent(self, user_message: str) -> ShoppingIntent:
        pass