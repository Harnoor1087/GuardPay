from fastapi import APIRouter, Depends

from backend.app.api.dependencies import get_shopping_service
from backend.app.schemas.api import SearchRequest, SearchResponse
from backend.app.services.shopping import ShoppingService


router = APIRouter(
    prefix="/api/v1",
    tags=["search"],
)


@router.post(
    "/search",
    response_model=SearchResponse,
)
def search(
    request: SearchRequest,
    shopping_service: ShoppingService = Depends(get_shopping_service),
):
    return shopping_service.search(request.message)