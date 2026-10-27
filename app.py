from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/message")
def message():
    return "this message from Python courtesy of Flask"

if __name__ == "__main__":
    app.run(debug=True)