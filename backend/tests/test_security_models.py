import pytest
from pydantic import ValidationError

from backend.app.security.models import (
    SecurityDecision,
    SecurityResult,
    SecuritySignal,
)


def test_security_result_defaults_to_empty_signals():

    result = SecurityResult(
        decision=SecurityDecision.ALLOW,
        risk_score=0,
    )

    assert result.decision == SecurityDecision.ALLOW
    assert result.risk_score == 0
    assert result.signals == []


def test_security_signal_accepts_valid_score():

    signal = SecuritySignal(
        name="instruction_override",
        description="Attempt to override instructions",
        score=40,
    )

    assert signal.score == 40


def test_risk_score_cannot_exceed_100():

    with pytest.raises(ValidationError):

        SecurityResult(
            decision=SecurityDecision.BLOCK,
            risk_score=101,
        )


def test_risk_score_cannot_be_negative():

    with pytest.raises(ValidationError):

        SecurityResult(
            decision=SecurityDecision.BLOCK,
            risk_score=-1,
        )