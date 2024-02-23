#!/usr/bin/python3
""" returns a JSON: 'status': 'OK """


from api.v1.views import app_views
from flask import jsonify, request
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.user import User
from models.state import State
from models.review import Review


@app_views.route("/status", methods=["GET"])
def status_api():
    """returns status route OK for GET method"""
    if request.method == "GET":
        return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"])
def stats_get():
    """Retrieves the number of each objects by type"""
    if request.method == "GET":
        response = {
            "amenities": storage.count(Amenity),
            "cities": storage.count(City),
            "places": storage.count(Place),
            "reviews": storage.count(Review),
            "states": storage.count(State),
            "users": storage.count(User),
        }
        return jsonify(response)
