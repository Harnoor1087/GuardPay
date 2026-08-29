from backend.app.security.models import (
    SecurityDecision,
    SecurityResult,
    SecuritySignal,
)


class SecurityPolicy:

    REVIEW_THRESHOLD = 30
    BLOCK_THRESHOLD = 60

    def evaluate(
        self,
        signals: list[SecuritySignal],
    ) -> SecurityResult:

        total_score = sum(
            signal.score
            for signal in signals
        )

        risk_score = min(total_score, 100)

        if risk_score >= self.BLOCK_THRESHOLD:
            decision = SecurityDecision.BLOCK

        elif risk_score >= self.REVIEW_THRESHOLD:
            decision = SecurityDecision.REVIEW

        else:
            decision = SecurityDecision.ALLOW

        return SecurityResult(
            decision=decision,
            risk_score=risk_score,
            signals=signals,
        )