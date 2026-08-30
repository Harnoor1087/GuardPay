import logging

from backend.app.security.models import SecurityResult


logger = logging.getLogger(__name__)


class SecurityAuditLogger:

    def record(
        self,
        request_id: str,
        result: SecurityResult,
    ) -> None:

        try:

            logger.info(
                "security_decision "
                "request_id=%s decision=%s risk_score=%s",
                request_id,
                result.decision.value,
                result.risk_score,
            )

        except Exception:

            logger.exception(
                "security_audit_failed "
                "request_id=%s",
                request_id,
            )