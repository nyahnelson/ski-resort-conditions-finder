
from flask import abort, Blueprint, jsonify, render_template, request
from src.api.controller import get_all_resorts, get_resort_by_id, get_forecasts_by_resort
from datetime import date

from src.api.controller import (
    get_average_temperature,
    get_resort_by_id
)

api_bp = Blueprint("api", __name__)

@api_bp.route("/", methods=["GET"])
def home():
    resorts = get_all_resorts()
    return render_template("index.html", resorts=resorts)


@api_bp.route("/conditions")
def conditions():
    resort_id = request.args.get("resort_id", type=int)

    resort = get_resort_by_id(resort_id)

    if resort is None:
        abort(404)

    forecasts = get_forecasts_by_resort(resort_id)

    return render_template(
        "conditions.html",
        resort=resort,
        forecasts=forecasts
    )


@api_bp.route("/api/resorts", methods=["GET"])
def resorts():
    return jsonify({"resorts": get_all_resorts()})

@api_bp.route("/api/resorts/<int:resort_id>", methods=["GET"])
def resort_details(resort_id):
    resort = get_resort_by_id(resort_id)

    if resort is None:
        return jsonify({"error": "Resort not found"}), 404

    return jsonify(resort)

@api_bp.route(
    "/api/resorts/<int:resort_id>/average-temperature",
    methods=["GET"]
)
def average_temperature(resort_id):
    start = request.args.get("start_date")
    end = request.args.get("end_date")

    if not start or not end:
        return jsonify({
            "error": "start_date and end_date are required"
        }), 400

    try:
        start_date = date.fromisoformat(start)
        end_date = date.fromisoformat(end)
    except ValueError:
        return jsonify({
            "error": "Dates must use YYYY-MM-DD format"
        }), 400

    if start_date > end_date:
        return jsonify({
            "error": "start_date must be before or equal to end_date"
        }), 400

    if get_resort_by_id(resort_id) is None:
        return jsonify({"error": "Resort not found"}), 404

    result = get_average_temperature(
        resort_id,
        start_date,
        end_date
    )

    return jsonify(result), 200