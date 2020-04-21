#!/usr/bin/python3
""" script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
You must use storage for fetching data from the storage engine
(FileStorage or DBStorage) => from models import storage and storage.all(...)
After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)

@app.teardown_appcontext
def tear_down(self):
    """After each request removes the current SQLAlchemy Session.
    """
    storage.close()

@app.route('/states_list', strict_slashes=False)
def list_states():
    states_dict = storage.all(State)
    states_listed = []
    for k, v in states_dict.items():
        states_listed.append(v)
    return render_template('7-states_list', states_listed=states_listed)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
