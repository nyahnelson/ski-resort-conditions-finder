
from flask import abort, Blueprint, jsonify, render_template, request
from src.api.controller import get_all_resorts, get_resort_by_id, get_forecasts_by_resort

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
