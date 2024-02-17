#!/usr/bin/python3
"""
Python script that starts a Flask web application:
"""
from flask import Flask


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
def display_is_magic(text):
    """
    return "is magic"
    """
    return 'Python ' + text.replace('_', ' ')

if __name__ == "__main__":
    """
    main console
    """
    
    print("* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)")
    app.run(host='0.0.0.0', port=5000)