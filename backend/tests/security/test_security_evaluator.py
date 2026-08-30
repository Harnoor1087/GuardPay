from backend.app.security.evaluation.evaluator import (
    SecurityEvaluator,
)
from backend.app.security.prompt_injection import (
    PromptInjectionDetector,
)


def test_security_evaluator_counts_results():

    detector = PromptInjectionDetector()

    evaluator = SecurityEvaluator(detector)

    metrics = evaluator.evaluate()

    assert metrics.true_positives > 0
    assert metrics.true_negatives > 0

    assert metrics.false_positives == 0
    assert metrics.false_negatives == 0


def test_detection_rate():

    detector = PromptInjectionDetector()

    evaluator = SecurityEvaluator(detector)

    metrics = evaluator.evaluate()

    assert metrics.detection_rate == 1.0


def test_false_positive_rate():

    detector = PromptInjectionDetector()

    evaluator = SecurityEvaluator(detector)

    metrics = evaluator.evaluate()

    assert metrics.false_positive_rate == 0.0