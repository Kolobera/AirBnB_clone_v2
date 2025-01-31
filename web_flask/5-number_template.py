#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_text(text):
    """Display C with text"""
    text = text.replace("_", " ")
    return 'C %s' % text


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_ptext(text="is cool"):
    """Display Python with text"""
    text = text.replace("_", " ")
    return 'Python %s' % text


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' only if n is an integer."""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def numbern(n):
    """Displays 'n is a number' only if n is an integer."""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
