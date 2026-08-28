from pydantic import BaseModel, Field

from backend.app.schemas.product import Product


class RankingBreakdown(BaseModel):
    rating: float = Field(ge=0, le=1)
    popularity: float = Field(ge=0, le=1)
    price: float = Field(ge=0, le=1)
    feature_match: float = Field(ge=0, le=1)


class RankedProduct(BaseModel):
    product: Product
    score: float = Field(ge=0, le=1)
    breakdown: RankingBreakdown
    explanation: str