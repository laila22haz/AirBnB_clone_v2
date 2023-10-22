#!/usr/bin/python3
""" Starts a Flask web application"""""

from flask import *
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    cities = storage.all(City).values()
    sorted_cities = sorted(cities, key=lambda city: city.name)
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html',
                           cities=sorted_cities, states=sorted_states)


@app.teardown_appcontext
def teardown_db(self):
    """close Session"""
    storage.close()


if __name__ == '__main__':
    """ Makes the app run when called from the command line"""
    app.run(host='0.0.0.0', port=5000)
