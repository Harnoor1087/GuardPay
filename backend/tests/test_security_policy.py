from backend.app.security.models import (
    SecurityDecision,
    SecuritySignal,
)
from backend.app.security.policy import SecurityPolicy


policy = SecurityPolicy()


def make_signal(score: int) -> SecuritySignal:
    return SecuritySignal(
        name="test_signal",
        description="Test security signal",
        score=score,
    )


def test_no_signals_are_allowed():

    result = policy.evaluate([])

    assert result.decision == SecurityDecision.ALLOW
    assert result.risk_score == 0
    assert result.signals == []


def test_score_below_review_threshold_is_allowed():

    result = policy.evaluate([
        make_signal(29),
    ])

    assert result.decision == SecurityDecision.ALLOW
    assert result.risk_score == 29


def test_review_threshold_returns_review():

    result = policy.evaluate([
        make_signal(30),
    ])

    assert result.decision == SecurityDecision.REVIEW
    assert result.risk_score == 30


def test_score_below_block_threshold_returns_review():

    result = policy.evaluate([
        make_signal(59),
    ])

    assert result.decision == SecurityDecision.REVIEW
    assert result.risk_score == 59


def test_block_threshold_returns_block():

    result = policy.evaluate([
        make_signal(60),
    ])

    assert result.decision == SecurityDecision.BLOCK
    assert result.risk_score == 60


def test_multiple_signals_are_combined():

    result = policy.evaluate([
        make_signal(40),
        make_signal(30),
    ])

    assert result.decision == SecurityDecision.BLOCK
    assert result.risk_score == 70


def test_risk_score_is_capped_at_100():

    result = policy.evaluate([
        make_signal(80),
        make_signal(50),
    ])

    assert result.decision == SecurityDecision.BLOCK
    assert result.risk_score == 100