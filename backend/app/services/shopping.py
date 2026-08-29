from backend.app.llm.intent_extractor import IntentExtractor
from backend.app.services.search import ProductSearchService
from backend.app.services.ranking import ProductRankingService
from backend.app.security.gateway import SecurityGateway
from backend.app.security.models import SecurityDecision
from backend.app.security.exceptions import SecurityBlockedError


class ShoppingService:

    def __init__(
        self,
        intent_extractor: IntentExtractor,
        search_service: ProductSearchService,
        ranking_service: ProductRankingService,
        security_gateway: SecurityGateway,
        products,
    ):
        self.intent_extractor = intent_extractor
        self.search_service = search_service
        self.ranking_service = ranking_service
        self.security_gateway = security_gateway
        self.products = products

    def search(self, user_message: str):

        security_result = self.security_gateway.check(
            user_message
        )

        if security_result.decision == SecurityDecision.BLOCK:
            raise SecurityBlockedError()

        intent = self.intent_extractor.extract(
            user_message
        )

        products = self.search_service.search(
            self.products,
            category=intent.category,
            max_price=intent.max_price,
            brand=intent.brand,
        )

        ranked_products = self.ranking_service.rank(
            products,
            preferred_use_case=intent.use_case,
        )

        return {
            "intent": intent,
            "products": ranked_products,
            "security": security_result,
        }