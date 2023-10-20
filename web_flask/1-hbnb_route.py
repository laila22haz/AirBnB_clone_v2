#!/usr/bin/python3
"""
This module defines a simple Flask application that greets the user.
"""

from flask import Flask

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


if __name__ == '__main__':
    app.run(debug=True)
