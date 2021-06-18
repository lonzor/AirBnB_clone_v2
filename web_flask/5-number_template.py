#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from flask import render_template


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


@app.route('/c/<text>')
def display_prompt3(text):
    """Displays prompt C <text>"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/<string:text>')
@app.route('/python/')
def display_prompt4(text='is cool'):
    """Displays Python praising text"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>')
def is_a_num(n):
    """Displays if n is a number or not"""
    return '%i is a number' % n


@app.route('/number_template/<int:n>')
def template_is_a_num(n):
    """Displays html template if n is a number"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
