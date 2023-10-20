#!/usr/bin/python3
"""
This module defines a simple Flask application that greets the user.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    This function handles the root URL of the Flask application.

    Returns:
        str: A simple greeting message.
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This function handles the root URL of the Flask application.

    Returns:
        str: A simple greeting message.
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    """
    This function handles the root URL of the Flask application.

    Returns:
        str: A simple greeting message.
    """
    return f'C %s' % text.replace('_', ' ')


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def Python_cool(text='is cool'):
    """
    This function handles the root URL of the Flask application.

    Returns:
        str: A simple greeting message.
    """
    return f'Python %s' % text.replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def is_integer(n):
    """
    This function handles the root URL of the Flask application.

    Returns:
        str: A simple greeting message.
    """
    return f'%d is a number' % n


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_templete(n=None):
    """
    This function handles the root URL of the Flask application.

    Returns:
        str: A simple greeting message.
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    """
    This function handles the root URL of the Flask application.

    Returns:
        str: HTML page with the number and its even/odd status.
    """
    result = "even" if n % 2 == 0 else "odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == '__main__':
    app.run(debug=True)
