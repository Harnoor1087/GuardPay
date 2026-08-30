from pydantic import BaseModel, Field, field_validator

from backend.app.schemas.ranking import RankedProduct
from backend.app.schemas.intent import ShoppingIntent


class SearchRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=2000,
        description="Natural-language shopping request",
    )

    @field_validator("message")
    @classmethod
    def validate_message(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Search message cannot be empty")

        return value

class SecurityResponse(BaseModel):
    decision: str
    risk_score: int = Field(ge=0, le=100)

class SearchResponse(BaseModel):
    intent: ShoppingIntent
    products: list[RankedProduct]
    security: SecurityResponse