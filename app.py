from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <h1>Demostración CI/CD con Docker</h1>
    <p>Aplicación desplegada en Ubuntu Server.</p>
    <p>Versión 1.0</p>
    """

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
