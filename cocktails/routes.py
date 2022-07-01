from flask import render_template
from cocktails import app, all_cocktails


@app.route("/")
def main():
    return render_template("index.html", cocktails=all_cocktails)

