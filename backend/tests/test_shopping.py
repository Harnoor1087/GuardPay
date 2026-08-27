from backend.app.llm.intent_extractor import IntentExtractor
from backend.app.llm.mock_provider import MockLLMProvider
from backend.app.services.catalog import ProductCatalog
from backend.app.services.search import ProductSearchService
from backend.app.services.shopping import ShoppingService


def test_end_to_end_shopping_search():

    catalog = ProductCatalog("data/products.json")

    provider = MockLLMProvider()
    intent_extractor = IntentExtractor(provider)

    search_service = ProductSearchService()

    shopping_service = ShoppingService(
        intent_extractor=intent_extractor,
        search_service=search_service,
        products=catalog.get_all_products(),
    )

    result = shopping_service.search(
        "Find me Nike running shoes under 5000 for road running."
    )

    assert result["intent"].category == "running_shoes"
    assert result["intent"].brand == "Nike"
    assert result["intent"].max_price == 5000

    assert len(result["products"]) == 3

    for product in result["products"]:
        assert product.brand == "Nike"
        assert product.price <= 5000