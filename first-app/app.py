from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    version = "v1.0.0"  # Change this to test deployments
    calling-branch = os.getenv("CALLING_BRANCH, "unknown-branch")
    return f"Hello, World! Running version {version}.\n This was published from branch {calling-branch}.\nalso, goodbye!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
