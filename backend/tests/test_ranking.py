from backend.app.services.catalog import ProductCatalog
from backend.app.services.ranking import ProductRankingService


def test_products_are_ranked():

    catalog = ProductCatalog("data/products.json")

    products = [
        product
        for product in catalog.get_all_products()
        if product.category == "running_shoes"
        and product.brand == "Nike"
        and product.price <= 5000
    ]

    ranking_service = ProductRankingService()

    ranked_products = ranking_service.rank(
        products,
        preferred_use_case="road",
    )

    assert len(ranked_products) == 3

    assert ranked_products[0].product.name == "Nike Pegasus 40"

    assert 0 <= ranked_products[0].score <= 1

    assert 0 <= ranked_products[0].breakdown.rating <= 1
    assert 0 <= ranked_products[0].breakdown.popularity <= 1
    assert 0 <= ranked_products[0].breakdown.price <= 1
    assert 0 <= ranked_products[0].breakdown.feature_match <= 1

def test_ranking_contains_explanation():

    catalog = ProductCatalog("data/products.json")

    products = [
        product
        for product in catalog.get_all_products()
        if product.category == "running_shoes"
        and product.brand == "Nike"
        and product.price <= 5000
    ]

    ranking_service = ProductRankingService()

    ranked_products = ranking_service.rank(
        products,
        preferred_use_case="road",
    )

    top_product = ranked_products[0]

    assert top_product.explanation
    assert isinstance(top_product.explanation, str)
    assert len(top_product.explanation) > 0