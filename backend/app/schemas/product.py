from pydantic import BaseModel, Field


class ProductAttributes(BaseModel):
    surface: list[str] | None = None
    waterproof: bool | None = None
    weight_grams: int | None = Field(default=None, gt=0)
    cushioning: str | None = None
    ram_gb: int | None = Field(default=None, gt=0)
    storage_gb: int | None = Field(default=None, gt=0)
    processor: str | None = None


class ShippingInfo(BaseModel):
    delivery_days: int = Field(gt=0)


class Product(BaseModel):
    id: str
    name: str
    brand: str
    category: str
    description: str
    price: float = Field(ge=0)
    currency: str
    rating: float = Field(ge=0, le=5)
    review_count: int = Field(ge=0)
    inventory: int = Field(ge=0)
    attributes: ProductAttributes
    shipping: ShippingInfo