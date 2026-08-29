class SecurityBlockedError(Exception):

    def __init__(
        self,
        message: str = "Request blocked by security policy.",
    ):
        self.message = message
        super().__init__(message)