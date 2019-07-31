#!/usr/bin/env python3

# An object of Flask class is our WSGI application
from flask import Flask

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/")
def hello_world():
   return "Hello World\n"

@app.route("/josh")
def whatsgoingon():
    return "Coming in hot!!\n"

@app.route("/hello/<name>")
def helloname(name):
    name = name.upper()
    name = name + " Would you like to play a game?"
    return "Hello {}\n".format(name)

if __name__ == "__main__":
   app.run(port=5009) # runs the application
   # app.run(port=5006, debug=True) # DEBUG MODE
