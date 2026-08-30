from backend.app.security.models import (
    SecurityDecision,
    SecuritySignal,
)
from backend.app.security.policy import SecurityPolicy


def test_no_signals_are_allowed():

    policy = SecurityPolicy()

    result = policy.evaluate([])

    assert result.risk_score == 0
    assert result.decision == SecurityDecision.ALLOW


def test_score_below_review_threshold_is_allowed():

    policy = SecurityPolicy()

    signals = [
        SecuritySignal(
            name="test_signal",
            description="Test signal",
            score=29,
        )
    ]

    result = policy.evaluate(signals)

    assert result.risk_score == 29
    assert result.decision == SecurityDecision.ALLOW


def test_review_threshold_is_inclusive():

    policy = SecurityPolicy()

    signals = [
        SecuritySignal(
            name="test_signal",
            description="Test signal",
            score=30,
        )
    ]

    result = policy.evaluate(signals)

    assert result.risk_score == 30
    assert result.decision == SecurityDecision.REVIEW


def test_score_between_thresholds_requires_review():

    policy = SecurityPolicy()

    signals = [
        SecuritySignal(
            name="test_signal",
            description="Test signal",
            score=59,
        )
    ]

    result = policy.evaluate(signals)

    assert result.risk_score == 59
    assert result.decision == SecurityDecision.REVIEW


def test_block_threshold_is_inclusive():

    policy = SecurityPolicy()

    signals = [
        SecuritySignal(
            name="test_signal",
            description="Test signal",
            score=60,
        )
    ]

    result = policy.evaluate(signals)

    assert result.risk_score == 60
    assert result.decision == SecurityDecision.BLOCK


def test_multiple_signals_are_aggregated():

    policy = SecurityPolicy()

    signals = [
        SecuritySignal(
            name="instruction_override",
            description="Instruction override",
            score=40,
        ),
        SecuritySignal(
            name="system_prompt_extraction",
            description="Prompt extraction",
            score=30,
        ),
    ]

    result = policy.evaluate(signals)

    assert result.risk_score == 70
    assert result.decision == SecurityDecision.BLOCK


def test_risk_score_is_capped_at_100():

    policy = SecurityPolicy()

    signals = [
        SecuritySignal(
            name="signal_one",
            description="First signal",
            score=80,
        ),
        SecuritySignal(
            name="signal_two",
            description="Second signal",
            score=50,
        ),
    ]

    result = policy.evaluate(signals)

    assert result.risk_score == 100
    assert result.decision == SecurityDecision.BLOCK