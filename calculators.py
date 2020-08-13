# calculators.py
# Calculators for recommending protein intake based on body weight.


def lbs_to_kg(lbs: float):
    '''Convert lbs to kg.'''
    return round(lbs / 2.205, 2)


def daily_protein(kg: float, activity_level: str):
    '''
    Return daily recommendation of protein based on weight and activity level.
    '''
    if activity_level == 'normal':
        return str(round(kg * 0.8)) + '-' + str(round(kg * 1.0))
    elif activity_level == 'endurance':
        return str(round(kg * 1.2)) + '-' + str(round(kg * 1.6))
    else:
        # activity_level == 'strength'
        return str(round(kg * 1.2)) + '-' + str(round(kg * 2.0))
