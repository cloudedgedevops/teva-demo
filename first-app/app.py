from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    version = "v1.0.0"  # Change this to test deployments
    return f"Hello, World! Running version {version}. also, goodbye!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
