#!/usr/bin/python3
""" Module for flask Application """


from models import storage
from api.v1.views import app_views
from os import environ
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, origins="0.0.0.0")


@app.teardown_appcontext
def stor_close(err):
    """method to handle @app.teardown_appcontext that calls storage.close()"""
    storage.close()


@app.errorhandler(404)
def not_found_err(err):
    """A handler for 404 errors that returns a JSON-formatted 404 status
    content : "error": "Not found" """
    return jsonify(error="Not found"), 404


if __name__ == "__main__":
    """ Run the Flask server (variable app) """
    host = environ.get('HBNB_API_HOST')
    if not host:
        host = '0.0.0.0'
    port = environ.get('HBNB_API_PORT')
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)