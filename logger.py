import json
from datetime import datetime


def log_event(event_type, request, severity="LOW"):
    """
    Logs security-relevant events in structured JSON format.
    No sensitive data is stored.
    """

    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "severity": severity,
        "source_ip": request.remote_addr,
        "http_method": request.method,
        "path": request.path,
        "user_agent": request.headers.get("User-Agent", "")[:200],
    }

    with open("security.log", "a", encoding="utf-8") as log_file:
        log_file.write(json.dumps(event) + "\n")
