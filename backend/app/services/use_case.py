USE_CASE_SURFACE_MAP = {
    "road_running": "road",
    "trail_running": "trail",
    "track_running": "track",
}


def normalize_use_case(use_case: str | None) -> str | None:
    if not use_case:
        return None

    normalized = use_case.strip().lower()

    return USE_CASE_SURFACE_MAP.get(
        normalized,
        normalized,
    )