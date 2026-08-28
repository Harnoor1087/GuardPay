from backend.app.schemas.ranking import RankedProduct


def generate_explanation(ranked_product: RankedProduct) -> str:
    breakdown = ranked_product.breakdown

    reasons = []

    if breakdown.rating >= 0.8:
        reasons.append("strong rating")

    if breakdown.popularity >= 0.8:
        reasons.append("strong review popularity")

    if breakdown.price >= 0.8:
        reasons.append("good price value")

    if breakdown.feature_match == 1.0:
        reasons.append("matches the requested use case")

    if not reasons:
        return "Recommended based on the overall ranking score."

    return "Recommended because of " + ", ".join(reasons) + "."