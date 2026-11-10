
from flask import Blueprint, jsonify, render_template, request
from src.api.controller import get_all_resorts, get_resort_by_id

api_bp = Blueprint("api", __name__)

@api_bp.route("/", methods=["GET"])
def home():
    resorts = get_all_resorts()
    return render_template("index.html", resorts=resorts)


@api_bp.route("/conditions", methods=["GET"])
def conditions():
    resort_id = request.args.get("resort_id", type=int)

    if resort_id is None:
        return "Please select a resort", 400

    resort = get_resort_by_id(resort_id)

    if resort is None:
        return "Resort not found", 404

    return render_template("conditions.html", resort=resort)


@api_bp.route("/api/resorts", methods=["GET"])
def resorts():
    return jsonify({"resorts": get_all_resorts()})

@api_bp.route("/api/resorts/<int:resort_id>", methods=["GET"])
def resort_details(resort_id):
    resort = get_resort_by_id(resort_id)

    if resort is None:
        return jsonify({"error": "Resort not found"}), 404

    return jsonify(resort)
