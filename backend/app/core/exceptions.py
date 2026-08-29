class GuardPayError(Exception):
    """Base exception for expected GuardPay application errors."""


class InternalServiceError(GuardPayError):
    """Raised when an internal service fails unexpectedly."""