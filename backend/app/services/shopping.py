from backend.app.llm.intent_extractor import IntentExtractor
from backend.app.services.search import ProductSearchService


class ShoppingService:

    def __init__(
        self,
        intent_extractor: IntentExtractor,
        search_service: ProductSearchService,
        products,
    ):
        self.intent_extractor = intent_extractor
        self.search_service = search_service
        self.products = products

    def search(self, user_message: str):

        intent = self.intent_extractor.extract(user_message)

        products = self.search_service.search(
            self.products,
            category=intent.category,
            max_price=intent.max_price,
            brand=intent.brand,
        )

        return {
            "intent": intent,
            "products": products,
        }