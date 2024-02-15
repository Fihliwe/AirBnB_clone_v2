#!/usr/bin/python3
"""
Python script that starts flask web app on port 5000 
"""
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    returns hello_hbnb
    """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    """
    return HBNB
    """
    return "HBNB"

if __name__ == "__main__":
    """
    main console
    """
    print("* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)")
    app.run(host='0.0.0.0', port=5000)