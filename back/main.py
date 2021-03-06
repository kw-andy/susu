import json
import logging
from typing import Tuple

from flask import Flask, jsonify, Response
from flask_cors import cross_origin
from werkzeug.exceptions import InternalServerError

from store.rides import RideService, RideNotFound

app = Flask(__name__)
logger = logging.getLogger(__name__)

APIResponse = Tuple[Response, int]


@app.errorhandler(InternalServerError)
def handle_exception(e: InternalServerError) -> APIResponse:
    return (
        json.dumps({"error": "internal_error", "message": "Internal error"}),
        500,
    )


@app.route("/rides", methods=["GET"])
@cross_origin()
def get_all_rides() -> APIResponse:
    all_rides = RideService.get_all()
    return jsonify(all_rides), 200


@app.route("/rides/<int:ride_id>", methods=["GET"])
@cross_origin()
def get_ride(ride_id: int) -> APIResponse:
    try:
        ride = RideService.get(ride_id)
        return jsonify(ride), 200
    except RideNotFound:
        return (
            jsonify(
                {"error": "ride_not_found", "message": f"Ride {ride_id} not found"}
            ),
            404,
        )


if __name__ == "__main__":
    app.run()
