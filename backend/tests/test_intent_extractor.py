from backend.app.llm.intent_extractor import IntentExtractor
from backend.app.llm.mock_provider import MockLLMProvider


provider = MockLLMProvider()
extractor = IntentExtractor(provider)

intent = extractor.extract(
    "I want Nike running shoes for road running under 5000 rupees."
)

print(intent)
print(intent.model_dump())