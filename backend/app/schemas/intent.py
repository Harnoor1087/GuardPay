from pydantic import BaseModel, Field


class ShoppingIntent(BaseModel):
    category: str | None = None
    max_price: float | None = Field(default=None, ge=0)
    min_price: float | None = Field(default=None, ge=0)
    brand: str | None = None
    use_case: str | None = None
    waterproof: bool | None = None