from flask import abort
from logger import log_event


def fake_admin_endpoint(request):
    """
    Honeypot endpoint.
    This endpoint must never succeed.
    """

    log_event(
        event_type="HONEYPOT_FAKE_ADMIN_ENDPOINT_ACCESSED",
        request=request,
        severity="HIGH"
    )

    abort(403)


def detect_suspicious_input(request):
    """
    Detects simple suspicious input patterns.
    Observation only - no blocking, no sanitization.
    """

    raw_data = request.get_data(as_text=True)

    if not raw_data:
        return

    indicators = ["' or ", "union select", "<script", "--"]
    lowered = raw_data.lower()

    for indicator in indicators:
        if indicator.lower() in raw_data.lower():
            log_event(
                event_type="HONEYPOT_SUSPICIOUS_INPUT_DETECTED",
                request=request,
                severity="MEDIUM"
            )
            break
