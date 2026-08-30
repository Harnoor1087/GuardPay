from backend.app.security.evaluation.evaluator import (
    EvaluationMetrics,
)
from backend.app.security.evaluation.reporter import (
    SecurityEvaluationReporter,
)


def test_security_report_contains_metrics():

    metrics = EvaluationMetrics(
        true_positives=6,
        true_negatives=3,
        false_positives=0,
        false_negatives=0,
    )

    report = SecurityEvaluationReporter.generate(metrics)

    assert "True Positives:      6" in report
    assert "True Negatives:      3" in report
    assert "False Positives:     0" in report
    assert "False Negatives:     0" in report

    assert "Detection Rate:      100.00%" in report
    assert "False Positive Rate: 0.00%" in report

    assert "Status: PASS" in report


def test_security_report_fails_when_errors_exist():

    metrics = EvaluationMetrics(
        true_positives=5,
        true_negatives=2,
        false_positives=1,
        false_negatives=1,
    )

    report = SecurityEvaluationReporter.generate(metrics)

    assert "Detection Rate:      83.33%" in report
    assert "False Positive Rate: 33.33%" in report

    assert "Status: FAIL" in report