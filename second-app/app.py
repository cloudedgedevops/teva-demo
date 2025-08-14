import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    version = "v2.0.0"  # Change this to test deployments
    calling_branch = os.getenv("CALLING_BRANCH", "unknown-branch")
    return f"greetins, World! this is my second app, Running version {version}.\n This was published from branch {calling_branch}.\nalso, goodbye!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
