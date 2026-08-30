from backend.app.security.evaluation.evaluator import (
    EvaluationMetrics,
)


class SecurityEvaluationReporter:

    @staticmethod
    def generate(metrics: EvaluationMetrics) -> str:

        detection_rate = metrics.detection_rate * 100
        false_positive_rate = metrics.false_positive_rate * 100

        status = (
            "PASS"
            if metrics.false_negatives == 0
            and metrics.false_positives == 0
            else "FAIL"
        )

        return (
            "GuardPay Security Evaluation\n"
            "─────────────────────────────\n\n"
            f"True Positives:      {metrics.true_positives}\n"
            f"True Negatives:      {metrics.true_negatives}\n"
            f"False Positives:     {metrics.false_positives}\n"
            f"False Negatives:     {metrics.false_negatives}\n\n"
            f"Detection Rate:      {detection_rate:.2f}%\n"
            f"False Positive Rate: {false_positive_rate:.2f}%\n\n"
            f"Status: {status}"
        )