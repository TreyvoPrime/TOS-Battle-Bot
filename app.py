from flask import Flask, render_template
import os

# Initialize Flask app
app = Flask(__name__)

# =========================
# ROUTES
# =========================

@app.route("/")
def home():
    return "Battle Alert Bot is running."

@app.route("/terms")
def terms():
    return render_template("tos.html")

# (Optional) Privacy route if you add it later
@app.route("/privacy")
def privacy():
    return "Privacy Policy coming soon."

# =========================
# RUN (only for local dev)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
