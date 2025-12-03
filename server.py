# Import the Flask class from the flask module
from flask import Flask, jsonify


# Create an instance of the Flask class
# , passing in the name of the current module
app = Flask(__name__)


# Define a route for the root URL ("/")
@app.route("/")
def home():
    # Function that handles requests to the root URL
    return jsonify("Hello, World!")


@app.route("/no_content")
def no_content():
    # Function that handles requests to the "/no_content" URL
    return ({'message': 'No content'}, 204)  # Return a 204 No Content response
