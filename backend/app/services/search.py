from backend.app.schemas.product import Product


class ProductSearchService:

    def search(
        self,
        products: list[Product],
        category: str | None = None,
        max_price: float | None = None,
        brand: str | None = None,
        in_stock_only: bool = True,
    ) -> list[Product]:

        results = products

        if category:
            results = [
                product
                for product in results
                if product.category.lower() == category.lower()
            ]

        if max_price is not None:
            results = [
                product
                for product in results
                if product.price <= max_price
            ]

        if brand:
            results = [
                product
                for product in results
                if product.brand.lower() == brand.lower()
            ]

        if in_stock_only:
            results = [
                product
                for product in results
                if product.inventory > 0
            ]

        return results