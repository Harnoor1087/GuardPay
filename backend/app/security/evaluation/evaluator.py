from dataclasses import dataclass

from backend.app.security.prompt_injection import (
    PromptInjectionDetector,
)
from backend.app.security.evaluation.dataset import (
    SECURITY_TEST_CASES,
)


@dataclass(frozen=True)
class EvaluationMetrics:
    true_positives: int
    true_negatives: int
    false_positives: int
    false_negatives: int

    @property
    def detection_rate(self) -> float:
        total_attacks = self.true_positives + self.false_negatives

        if total_attacks == 0:
            return 0.0

        return self.true_positives / total_attacks

    @property
    def false_positive_rate(self) -> float:
        total_benign = self.true_negatives + self.false_positives

        if total_benign == 0:
            return 0.0

        return self.false_positives / total_benign


class SecurityEvaluator:

    def __init__(self, detector: PromptInjectionDetector):
        self.detector = detector

    def evaluate(self) -> EvaluationMetrics:

        true_positives = 0
        true_negatives = 0
        false_positives = 0
        false_negatives = 0

        for case in SECURITY_TEST_CASES:

            signals = self.detector.detect(case.text)

            detected = bool(signals)

            if case.expected_detection and detected:
                true_positives += 1

            elif not case.expected_detection and not detected:
                true_negatives += 1

            elif not case.expected_detection and detected:
                false_positives += 1

            elif case.expected_detection and not detected:
                false_negatives += 1

        return EvaluationMetrics(
            true_positives=true_positives,
            true_negatives=true_negatives,
            false_positives=false_positives,
            false_negatives=false_negatives,
        )