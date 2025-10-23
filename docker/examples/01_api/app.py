from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return "Hola mundo desde Flask (Docker)!"


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    # Solo para desarrollo local; en producción usa Gunicorn (ver Dockerfile)
    app.run(host="0.0.0.0", port=5000)
