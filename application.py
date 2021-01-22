from flask import Flask, render_template, url_for
from jinja2 import Markup
from myParser import device1Name

print(device1Name)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/devices')
def device():
    return render_template("template.html", device=device1Name)


if __name__== "__main__":
    app.run()

