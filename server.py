"""
This module provides a simple Flask application with a few routes.
"""
from flask import Flask, jsonify, make_response, request


app = Flask(__name__)


data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]


@app.route("/")
def home():
    """Handles requests to the root URL.

    Returns:
        A JSON response with "Hello, World!".
    """
    return jsonify("Hello, World!")


@app.route("/no_content")
def no_content():
    """Handles requests to the "/no_content" URL.

    Returns:
        A JSON response with "No content" and a 204 status code.
    """
    return {"message": "No content"}, 204


@app.route("/exp")
def exp():
    """Returns 'Hello World' message with a status code of 200.

    Returns:
        A Flask response with "Hello World" and a 200 status code.
    """
    resp = make_response({"message": "Hello World"})
    resp.status_code = 200
    return resp


@app.route("/data")
def get_data():
    """Handles requests to the "/data" URL.

    Returns:
        A JSON response with data information or an error message.
    """
    if data:
        return {"message": f"Data of length {len(data)} found"}
    return {"message": "Data is empty"}, 500


@app.route("/name_search")
def name_search():
    """Find a person in the database based on the provided query parameter.

    Returns:
        tuple:
        A JSON response with the person\'s data and a 200 status code if found.
        A JSON response with an error message and a 400,
        422, or 404 status code otherwise.
    """
    query = request.args.get("q")

    if query is None:
        return ({"message": "Missing 'q' param"},
                400)

    if not query.strip() or query.isdigit():
        return ({"message": "Invalid 'q' param"},
                422)

    for person in data:
        if query.lower() in person["first_name"].lower():
            return person, 200

    return ({"message": "Person not found"},
            404)


@app.route("/count")
def count():
    """Returns the number of items in the data list.

    Returns:
        A JSON response with the count of items in the data list.
    """
    return {"data_count": len(data)}
