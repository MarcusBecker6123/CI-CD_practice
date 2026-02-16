import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    domain = os.getenv("DOMAIN_NAME", "Localhost (Dev)")
    if domain == "Localhost (Dev)":
        return f"Warnung: DOMAIN_NAME nicht gesetzt! (Laufend auf {domain})"
    return f"Hello, AWS Practice! Running on {domain}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
