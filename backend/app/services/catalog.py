import json
from pathlib import Path

from backend.app.schemas.product import Product


class ProductCatalog:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
        self.products = self._load_products()

    def _load_products(self) -> list[Product]:
        with self.data_path.open("r", encoding="utf-8") as file:
            raw_products = json.load(file)

        return [Product.model_validate(product) for product in raw_products]

    def get_all_products(self) -> list[Product]:
        return self.products