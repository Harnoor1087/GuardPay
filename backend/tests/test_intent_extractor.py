from backend.app.llm.intent_extractor import IntentExtractor


extractor = IntentExtractor()

intent = extractor.extract(
    "I want Nike running shoes for road running under 5000 rupees."
)

print(intent)
print(intent.model_dump())