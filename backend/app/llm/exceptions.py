class LLMProviderError(Exception):

    def __init__(
        self,
        message: str = "LLM provider is unavailable.",
    ):
        self.message = message
        super().__init__(message)