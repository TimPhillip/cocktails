from flask import render_template
from cocktails import app, all_cocktails


@app.route("/")
def main():
    return render_template("index.html", cocktails=all_cocktails)

@app.route("/cocktail/<id>/")
def detailed_view(id=0):
    print(all_cocktails[int(id)])
    return render_template("cocktail.html", cocktail=all_cocktails[int(id)])

