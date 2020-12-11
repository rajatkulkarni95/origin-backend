from datetime import datetime


def calculate_risk_profile(data):
    try:
        age, dependents, house, income, marital_status, risk_questions, vehicle = data.values()
    except Exception as err:
        raise ValueError('Incomplete Input Data')

    risk_profile = {
        "auto": 0,
        "disability": 0,
        "home": 0,
        "life": 0,
    }
    base_score = sum(risk_questions)
    try:
        risk_profile = {key: base_score for key in risk_profile.keys()}

        # Age related Risks
        if age > 60:
            risk_profile['disability'] = 'ineligible'
            risk_profile['life'] = 'ineligible'

        if age < 30:
            risk_profile = {key: (value-2 if type(value) == int else value) for key,
                            value in risk_profile.items()}
        elif 30 < age < 40:
            risk_profile = {key: (value-1 if type(value) == int else value) for key,
                            value in risk_profile.items()}

        # Mortgage Related Risks
        if income > 200000:
            risk_profile = {key: (value-1 if type(value) == int else value) for key,
                            value in risk_profile.items()}

        if house['ownership_status'] == 'mortgaged':
            risk_profile['home'] += 1
            risk_profile['disability'] += 1

        # Life Related Risks
        if dependents > 0:
            risk_profile['life'] += 1
            risk_profile['disability'] += 1
        if marital_status == 'married':
            risk_profile['life'] += 1
            risk_profile['disability'] -= 1

        if vehicle['year'] > datetime.now().year - 5:
            risk_profile['auto'] += 1

        # Calculate the Risk Profile based on scores
        for key, value in risk_profile.items():
            if value <= 0:
                risk_profile[key] = 'economic'
            elif value == 1 or value == 2:
                risk_profile[key] = 'regular'
            elif value >= 3:
                risk_profile[key] = 'responsible'

        # Ineligibile Clauses
        if income == 0:
            risk_profile['disability'] = 'ineligible'

        if vehicle == 0:
            risk_profile['auto'] = 'ineligible'

        if house == 0:
            risk_profile['home'] = 'ineligible'

    except Exception as err:
        raise ValueError(err)

    return risk_profile
