from flask import Blueprint, request, jsonify, make_response
from flask_cors import CORS
from project.static.risk_algorithm import calculate_risk_profile

# Blueprint Config
risk_blueprint = Blueprint("risk_blueprint", __name__)
module = "Risk"
CORS(risk_blueprint)


@risk_blueprint.route('/risks', methods=['POST'])
def risk_assessment():
    input_data = request.get_json()
    risk_profile = calculate_risk_profile(input_data)

    res = make_response(jsonify(risk_profile), 200)
    return res
