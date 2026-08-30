from backend.app.security.audit import SecurityAuditLogger
from backend.app.security.models import (
    SecurityDecision,
    SecurityResult,
)


def test_security_audit_records_security_decision(caplog):

    logger = SecurityAuditLogger()

    result = SecurityResult(
        decision=SecurityDecision.BLOCK,
        risk_score=70,
        signals=[],
    )

    with caplog.at_level("INFO"):

        logger.record(
            request_id="test-request-123",
            result=result,
        )

    assert "security_decision" in caplog.text
    assert "request_id=test-request-123" in caplog.text
    assert "decision=block" in caplog.text
    assert "risk_score=70" in caplog.text


def test_security_audit_does_not_log_user_message(caplog):

    logger = SecurityAuditLogger()

    result = SecurityResult(
        decision=SecurityDecision.ALLOW,
        risk_score=0,
        signals=[],
    )

    sensitive_message = (
        "Find Nike shoes. SECRET_USER_DATA_12345"
    )

    with caplog.at_level("INFO"):

        logger.record(
            request_id="test-request-456",
            result=result,
        )

    assert sensitive_message not in caplog.text
    assert "SECRET_USER_DATA_12345" not in caplog.text

from fastapi.testclient import TestClient

from backend.app.main import app


client = TestClient(app)


def test_security_audit_uses_request_id(
    caplog,
):

    request_id = "audit-test-request-123"

    with caplog.at_level("INFO"):

        response = client.post(
            "/api/v1/search",
            headers={
                "X-Request-ID": request_id,
            },
            json={
                "message": "Find Nike running shoes under 5000",
            },
        )

    assert response.status_code == 200

    assert (
        response.headers["X-Request-ID"]
        == request_id
    )

    assert "security_decision" in caplog.text
    assert (
        f"request_id={request_id}"
        in caplog.text
    )

def test_audit_failure_does_not_raise(
    monkeypatch,
):

    logger_instance = SecurityAuditLogger()

    result = SecurityResult(
        decision=SecurityDecision.BLOCK,
        risk_score=70,
        signals=[],
    )

    def failing_log(*args, **kwargs):
        raise RuntimeError("Logging system unavailable")

    monkeypatch.setattr(
        "backend.app.security.audit.logger.info",
        failing_log,
    )

    logger_instance.record(
        request_id="audit-failure-test",
        result=result,
    )