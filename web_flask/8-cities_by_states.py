#!/usr/bin/python3
"""
This module defines Flask application.
"""

from flask import Flask, app, render_template
from models import storage
from models.state import State
#from models.city import City


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """
    This function handles the root URL of the Flask application.

    Returns:
        str: HTML page with list of Cities by states.
    """
    states = storage.all(State).values()
    #cities = storage.all(City).values()
    return render_template('8-cities_by_states.html\
                           ', states=states)


@app.teardown_appcontext
def after_request(_):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
