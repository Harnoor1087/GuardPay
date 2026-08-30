import pytest

from backend.app.llm.intent_extractor import IntentExtractor
from backend.app.schemas.intent import ShoppingIntent


class ValidProvider:

    def extract_intent(self, user_message: str):
        return ShoppingIntent(
            category="running_shoes",
            max_price=5000,
            brand="Nike",
        )


class InvalidProvider:

    def extract_intent(self, user_message: str):
        return {
            "category": "running_shoes",
            "max_price": 5000,
        }


def test_valid_provider_output_is_accepted():

    extractor = IntentExtractor(ValidProvider())

    result = extractor.extract(
        "Find Nike running shoes under 5000."
    )

    assert isinstance(result, ShoppingIntent)
    assert result.category == "running_shoes"
    assert result.max_price == 5000


def test_invalid_provider_output_is_rejected():

    extractor = IntentExtractor(InvalidProvider())

    with pytest.raises(TypeError, match="invalid intent"):

        extractor.extract(
            "Find Nike running shoes under 5000."
        )