from flask import Flask, jsonify, request
from honeypot import fake_admin_endpoint, detect_suspicious_input

app = Flask(__name__)


@app.before_request
def honeypot_inspection():
    """
    Honeypot inspection hook.
    This must not affect core application logic.
    """
    detect_suspicious_input(request)


@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok"}), 200


@app.route("/api/data", methods=["GET"])
def get_data():
    """
    Normal application endpoint.
    """
    return jsonify({"data": "public information"}), 200


@app.route("/api/admin/backup", methods=["GET"])
def admin_backup():
    """
    Honeypot endpoint.
    This endpoint is intentionally fake.
    """
    return fake_admin_endpoint(request)


@app.errorhandler(404)
def not_found(_):
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

