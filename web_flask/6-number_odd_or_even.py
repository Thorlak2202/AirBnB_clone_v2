#!/usr/bin/python3
""" script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>: display “C ” followed by the value of the text variable
/python/(<text>): display “Python ”, followed by the value of the text variable
The default value of text is “is cool”
You must use the option strict_slashes=False in your route definition
"""

from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def Hello_holby():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_is(text):
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/', defaults={'text': "is cool"})
@app.route('/python/<text>')
def python_is(text):
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_print(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def display_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def display_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(debug=True)
