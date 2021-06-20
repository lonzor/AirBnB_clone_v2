#!/usr/bin/python3
"""
Starts a flask app
Lists states from database from HTML template
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda x: x.name)
    return render_template('7-states_list.html', State=sorted_states)


@app.teardown_appcontext
def tear_down_db(exception):
    if storage:
        storage.close()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
