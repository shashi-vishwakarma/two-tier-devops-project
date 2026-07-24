from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Employee Management System</h1>
    <h3>Welcome to TechNova Solutions</h3>
    <p>Project: Two-Tier Docker & Jenkins Deployment</p>
    """

@app.route("/health")
def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)