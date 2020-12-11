from flask import Blueprint, request, jsonify, make_response
from flask_cors import CORS
from project.static.risk_algorithm import calculate_risk_profile

# Blueprint Config
risk_blueprint = Blueprint("risk_blueprint", __name__)
module = "Risk"
CORS(risk_blueprint)


@risk_blueprint.route('/risks', methods=['POST'])
def risk_assessment():
    try:
        input_data = request.get_json()
        risk_profile = calculate_risk_profile(input_data)

        res = make_response(jsonify(risk_profile), 200)
        return res
    except Exception as err:
        raise InvalidUsage(err, 500)


""" Exception Handling """


class InvalidUsage(Exception):
    status_code = 500

    def __init__(self, message, status_code):
        self.message = message

    def to_dict(self):
        ret = dict()
        ret['message'] = f'{self.message}'
        ret['status'] = self.status_code
        return ret


@risk_blueprint.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
