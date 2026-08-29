from pathlib import Path

from backend.app.llm.intent_extractor import IntentExtractor
from backend.app.llm.mock_provider import MockLLMProvider
from backend.app.services.catalog import ProductCatalog
from backend.app.services.search import ProductSearchService
from backend.app.services.ranking import ProductRankingService
from backend.app.services.shopping import ShoppingService
from backend.app.security.gateway import SecurityGateway
from backend.app.security.policy import SecurityPolicy
from backend.app.security.prompt_injection import PromptInjectionDetector


BASE_DIR = Path(__file__).resolve().parents[3]
PRODUCTS_PATH = BASE_DIR / "data" / "products.json"


catalog = ProductCatalog(str(PRODUCTS_PATH))

provider = MockLLMProvider()

intent_extractor = IntentExtractor(provider)

search_service = ProductSearchService()

ranking_service = ProductRankingService()

security_gateway = SecurityGateway(
    detectors=[
        PromptInjectionDetector(),
    ],
    policy=SecurityPolicy(),
)
    
shopping_service = ShoppingService(
    intent_extractor=intent_extractor,
    search_service=search_service,
    ranking_service=ranking_service,
    security_gateway=security_gateway,
    products=catalog.get_all_products(),
)


def get_shopping_service() -> ShoppingService:
    return shopping_service