from backend.app.security.detector import SecurityDetector
from backend.app.security.models import SecurityResult
from backend.app.security.policy import SecurityPolicy


class SecurityGateway:

    def __init__(
        self,
        detectors: list[SecurityDetector],
        policy: SecurityPolicy,
    ):
        self.detectors = detectors
        self.policy = policy

    def check(self, text: str) -> SecurityResult:

        signals = []

        for detector in self.detectors:
            signals.extend(
                detector.detect(text)
            )

        return self.policy.evaluate(signals)