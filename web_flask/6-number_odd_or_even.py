#!/usr/bin/python3
"""
Python script that starts a Flask web application:
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    display "hello hbnb"
    """
    return "Hello HBNB!"
    
@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """
    return HBNB
    """
    return "HBNB"

@app.route("/c/is_fun", strict_slashes=False)
def display_c():
    """
    return “C ” followed by the value of the text variable
    """
    return "C is fun"

@app.route("/c/<text>", strict_slashes=False)
def display_c_is_cool(text):
    """
    return c cool
    """
    return 'C ' + text.replace('_', ' ')

@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def display_is_magic(text="is cool"):
    """
    return "is magic"
    """
    return 'Python ' + text.replace('_', ' ')

@app.route("/number/<int:n>", strict_slashes=False)
def display_integer(n):
    """
    display n is a number
    """
    return "{:d} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def display_number_template(n):
    """
    display a HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def numbersandevenness(n):
    """display a HTML page only if n is an integer"""
    if n % 2 == 0:
        evenness = 'even'
    else:
        evenness = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, evenness=evenness)

if __name__ == "__main__":
    """
    main console
    """
    
    print("* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)")
    app.run(host='0.0.0.0', port=5000)