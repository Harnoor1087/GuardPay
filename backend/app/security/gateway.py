from backend.app.security.detector import SecurityDetector
from backend.app.security.models import (SecurityDecision, SecurityResult)
from backend.app.security.policy import SecurityPolicy
import logging
logger = logging.getLogger(__name__)

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

        try:
            for detector in self.detectors:
                signals.extend(
                    detector.detect(text)
                )

        except Exception:
            logger.exception(
                "security_detector_failure"
            )

            return SecurityResult(
                decision=SecurityDecision.BLOCK,
                risk_score=100,
                signals=[],
            )

        return self.policy.evaluate(signals)