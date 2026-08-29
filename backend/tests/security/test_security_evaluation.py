from backend.app.security.evaluation.dataset import (
    SECURITY_TEST_CASES,
)
from backend.app.security.prompt_injection import (
    PromptInjectionDetector,
)


def test_security_dataset():

    detector = PromptInjectionDetector()

    for case in SECURITY_TEST_CASES:

        signals = detector.detect(case.text)

        detected = bool(signals)

        assert detected == case.expected_detection, (
            f"Unexpected result for category "
            f"'{case.category}': {case.text}"
        )