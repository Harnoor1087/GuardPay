from backend.app.schemas.product import Product
from backend.app.schemas.ranking import RankedProduct, RankingBreakdown
from backend.app.services.ranking_explanation import generate_explanation

class ProductRankingService:

    def rank(
        self,
        products: list[Product],
        preferred_use_case: str | None = None,
    ) -> list[RankedProduct]:

        if not products:
            return []

        max_rating = max(product.rating for product in products)
        min_rating = min(product.rating for product in products)

        max_reviews = max(product.review_count for product in products)
        min_reviews = min(product.review_count for product in products)

        max_price = max(product.price for product in products)
        min_price = min(product.price for product in products)

        def normalize(
            value: float,
            minimum: float,
            maximum: float,
        ) -> float:

            if maximum == minimum:
                return 1.0

            return (value - minimum) / (maximum - minimum)

        ranked_products = []

        for product in products:

            rating_score = normalize(
                product.rating,
                min_rating,
                max_rating,
            )

            popularity_score = normalize(
                product.review_count,
                min_reviews,
                max_reviews,
            )

            price_score = 1 - normalize(
                product.price,
                min_price,
                max_price,
            )

            feature_score = 0.0

            if preferred_use_case:
                surfaces = product.attributes.surface or []

                if preferred_use_case in surfaces:
                    feature_score = 1.0

            final_score = (
                0.50 * rating_score
                + 0.20 * popularity_score
                + 0.20 * price_score
                + 0.10 * feature_score
            )

            breakdown = RankingBreakdown(
                rating=rating_score,
                popularity=popularity_score,
                price=price_score,
                feature_match=feature_score,
            )

            ranked_product = RankedProduct(
                product=product,
                score=final_score,
                breakdown=breakdown,
                explanation="",
            )

            ranked_product.explanation = generate_explanation(
                ranked_product
            )

            ranked_products.append(ranked_product)

            ranked_products.sort(
            key=lambda item: item.score,
            reverse=True,
        )

        return ranked_products