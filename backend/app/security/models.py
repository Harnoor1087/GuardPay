from enum import Enum

from pydantic import BaseModel, Field


class SecurityDecision(str, Enum):
    ALLOW = "allow"
    REVIEW = "review"
    BLOCK = "block"


class SecuritySignal(BaseModel):
    name: str
    description: str
    score: int = Field(ge=0)


class SecurityResult(BaseModel):
    decision: SecurityDecision
    risk_score: int = Field(ge=0, le=100)
    signals: list[SecuritySignal] = Field(default_factory=list)