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

@app.route("/c/cool", strict_slashes=False)
def display_c_is_cool():
    """
    return c cool
    """
    return "C cool"