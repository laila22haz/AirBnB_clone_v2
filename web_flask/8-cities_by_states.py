#!/usr/bin/python3
"""
This module defines Flask application.
"""

from flask import Flask, app, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """
    Display a list of states and their associated cities.

    Returns:
        str: HTML page with the list of states and cities.
    """
    data = storage.all(State)
    states = data.values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_session(exeption):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
