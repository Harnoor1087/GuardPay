from abc import ABC, abstractmethod

from backend.app.security.models import SecuritySignal


class SecurityDetector(ABC):

    @abstractmethod
    def detect(self, text: str) -> list[SecuritySignal]:
        """
        Analyze untrusted text and return detected
        security signals.
        """
        raise NotImplementedError