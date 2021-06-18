#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def display_prompt():
    """Displays prompt Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_prompt2():
    """Displays prompt HBNB"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
