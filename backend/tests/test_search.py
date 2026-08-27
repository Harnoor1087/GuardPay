from backend.app.services.catalog import ProductCatalog
from backend.app.services.search import ProductSearchService


def test_search_nike_under_5000():
    catalog = ProductCatalog("data/products.json")
    search_service = ProductSearchService()

    results = search_service.search(
        catalog.get_all_products(),
        category="running_shoes",
        max_price=5000,
        brand="Nike",
    )

    assert len(results) == 3

    for product in results:
        assert product.brand == "Nike"
        assert product.price <= 5000
        assert product.category == "running_shoes"