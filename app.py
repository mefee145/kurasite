from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    fikstur = []
    if request.method == "POST":
        takimlar = request.form["takimlar"].split("\n")
        takimlar = [t.strip() for t in takimlar if t.strip()]
        random.shuffle(takimlar)

        for i in range(0, len(takimlar), 2):
            if i+1 < len(takimlar):
                fikstur.append((takimlar[i], takimlar[i+1]))
            else:
                fikstur.append((takimlar[i], "Bay"))

    return render_template("index.html", fikstur=fikstur)

if __name__ == "__main__":
    app.run(debug=True)
