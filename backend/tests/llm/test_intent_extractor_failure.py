import pytest

from backend.app.llm.exceptions import LLMProviderError
from backend.app.llm.intent_extractor import IntentExtractor


class FailingProvider:

    def extract_intent(self, user_message: str):
        raise RuntimeError("internal provider failure")


def test_provider_failure_is_wrapped():

    extractor = IntentExtractor(FailingProvider())

    with pytest.raises(
        LLMProviderError,
        match="LLM provider is unavailable.",
    ):
        extractor.extract(
            "Find Nike running shoes under 5000."
        )