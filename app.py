from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def next_page():
    height = int(request.form.get("height"))
    weight = int(request.form.get("weight"))
    bmi = weight / (height / 100) ** 2
    return render_template("next.html", bmi=bmi)


if __name__ == "__main__":
    app.run(debug=True)
