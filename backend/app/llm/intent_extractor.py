from openai import OpenAI

from backend.app.config import OPENAI_API_KEY
from backend.app.schemas.intent import ShoppingIntent


class IntentExtractor:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def extract(self, user_message: str) -> ShoppingIntent:

        response = self.client.responses.parse(
            model="gpt-4o",
            input=[
                {
                    "role": "system",
                    "content": (
                        "You extract shopping intent from user messages. "
                        "Return only information explicitly stated or strongly "
                        "implied by the user's request. "
                        "Do not invent preferences."
                    ),
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
            text_format=ShoppingIntent,
        )

        for output in response.output:
            if output.type != "message":
                continue

            for item in output.content:
                if item.type == "output_text" and item.parsed:
                    return item.parsed

        raise RuntimeError("Could not extract shopping intent")