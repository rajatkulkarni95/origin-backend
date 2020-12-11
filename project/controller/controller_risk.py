from flask import Blueprint, request, jsonify
from flask_cors import CORS

# Blueprint Config
risk_blueprint = Blueprint("risk_blueprint", __name__)
module = "Risk"
CORS(risk_blueprint)


@risk_blueprint.route('/risks', methods=['POST'])
def risk_assessment():
    pass
