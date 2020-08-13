# food_data_central.py
'''
Make requests to FoodData Central (FDC) for full nutrition
information of foods. File is only needed for requesting from FDC,
and is not needed in deployment.
'''

import json
import requests

from pprint import pprint

'''NOT NEEDED FOR DEPLOYMENT
REMOVE TO REQUEST MORE FOODS
from fdc_api_key import API_KEY
API_KEY = API_KEY
'''
# PLACEHOLDER
API_KEY = None

nutrient_ids = {
    '203': 'protein',
    '204': 'fat',
    '205': 'carbs',
    '208': 'calories',
    '269': 'sugar',
    '291': 'fiber',
    '301': 'calcium',
    '303': 'iron',
    '304': 'magnesium',
    '305': 'phosphorus',
    '306': 'potassium',
    '307': 'sodium',
    '309': 'zinc',
    '310': 'chromium',
    '312': 'copper',
    '314': 'iodine',
    '315': 'manganese',
    '317': 'selenium',
    '539': 'added_sugar',
    '601': 'cholesterol',
    '605': 'trans_fat',
    '606': 'saturated_fat',
    '619': 'omega_3',
    '645': 'mono_fat',
    '646': 'poly_fat',
}

# String of codes to pass as param in request.
nutrient_codes = ','.join(nutrient_ids.keys())

vitamin_ids = {
    '320': 'a',
    '323': 'e',
    '328': 'd',
    '401': 'c',
    '404': 'b1',
    '405': 'b2',
    '406': 'b3',
    '410': 'b5',
    '415': 'b6',
    '416': 'b7',
    '417': 'b9',
    '418': 'b12',
    '430': 'k',
}

# String of codes to pass as param in request.
vitamin_codes = ','.join(vitamin_ids.keys())


class Food():
    def __init__(self):
        self.id = 0
        self.name = ''
        self.data_type = ''
        self.protein = 0
        self.fat = 0
        self.carbs = 0
        self.calories = 0
        self.sugar = 0
        self.fiber = 0
        self.calcium = 0
        self.iron = 0
        self.magnesium = 0
        self.phosphorus = 0
        self.potassium = 0
        self.sodium = 0
        self.zinc = 0
        self.chromium = 0
        self.copper = 0
        self.iodine = 0
        self.manganese = 0
        self.selenium = 0
        self.added_sugar = 0
        self.cholesterol = 0
        self.trans_fat = 0
        self.saturated_fat = 0
        self.mono_fat = 0
        self.poly_fat = 0
        self.a = 0
        self.b1 = 0
        self.b2 = 0
        self.b3 = 0
        self.b5 = 0
        self.b6 = 0
        self.b7 = 0
        self.b9 = 0
        self.b12 = 0
        self.c = 0
        self.d = 0
        self.e = 0
        self.k = 0
        self.omega_3 = 0

    def set_values(self, nutrition_data):
        for key in nutrition_data:
            setattr(self, key, nutrition_data[key])

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}('f'{self.id}, {self.name})')


def get_food(id: int):
    '''
    Requests and pprints full entry information
    for a single food when passed fdcId.
    '''
    payload = {'api_key': API_KEY}
    url = 'https://api.nal.usda.gov/fdc/v1/food/' + str(id)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    fd = json.loads(response.text)
    pprint(fd)
    # return fd


def get_food_nutrients(id: int) -> Food:
    '''
    Return a Food object with nutrients pulled from FoodData Central API
    for a food passed in with fdcId.
    '''
    payload_1 = {
        'api_key': API_KEY,
        'format': 'abridged',
        'nutrients': nutrient_codes
                 }
    url = 'https://api.nal.usda.gov/fdc/v1/food/' + str(id)
    response = requests.get(url, params=payload_1)
    response.raise_for_status()
    fd = json.loads(response.text)

    food = Food()
    food.id = fd['fdcId']
    food.name = fd['description'].title()
    food.data_type = fd['dataType']

    food_nutrients = {}

    for item in fd['foodNutrients']:
        code = item['number']
        nutrient = nutrient_ids[code]
        amount = item['amount']
        food_nutrients[nutrient] = amount

    payload_2 = {
        'api_key': API_KEY,
        'format': 'abridged',
        'nutrients': vitamin_codes
                 }

    response_2 = requests.get(url, params=payload_2)
    response_2.raise_for_status()
    fd_2 = json.loads(response_2.text)

    for item in fd_2['foodNutrients']:
        code = item['number']
        nutrient = vitamin_ids[code]
        amount = item['amount']
        food_nutrients[nutrient] = amount

    food.set_values(food_nutrients)

    food = format_food(food)

    return food


def get_multiple_foods(ids: list) -> list:
    '''
    Return list of of Food objects requested by list of ids.
    '''
    foods = []
    for id in ids:
        foods.append(get_food_nutrients(id))

    for food in foods:
        if food.name.startswith("Trader Joe'S, "):
            food.name = food.name.replace("Trader Joe'S, ", "")

    return foods


def format_food(food) -> Food:
    '''
    Returns rounded nutrition information as reflected by
    typical nutrional labeling.
    '''
    food.protein = round(food.protein)
    food.fat = round(food.fat)
    food.carbs = round(food.carbs)
    food.calories = round(food.calories)
    food.sugar = round(food.sugar)
    food.fiber = round(food.fiber)
    food.calcium = round(food.calcium)
    food.iron = round(food.iron, 1)
    food.magnesium = round(food.magnesium)
    food.phosphorus = round(food.phosphorus)
    food.potassium = round(food.potassium)
    food.sodium = round(food.sodium)
    food.zinc = round(food.zinc, 1)
    food.chromium = round(food.chromium, 2)
    food.copper = round(food.copper, 1)
    food.iodine = round(food.iodine, 2)
    food.manganese = round(food.manganese, 2)
    food.selenium = round(food.selenium, 1)
    food.added_sugar = round(food.added_sugar)
    food.cholesterol = round(food.cholesterol)
    food.trans_fat = round(food.trans_fat)
    food.saturated_fat = round(food.saturated_fat)
    food.mono_fat = round(food.mono_fat)
    food.poly_fat = round(food.poly_fat)
    food.a = round(food.a)
    food.b1 = round(food.b1, 1)
    food.b2 = round(food.b2, 1)
    food.b3 = round(food.b3, 1)
    food.b5 = round(food.b5, 1)
    food.b6 = round(food.b6, 1)
    food.b7 = round(food.b7, 2)
    food.b9 = round(food.b9)
    food.b12 = round(food.b12, 2)
    food.c = round(food.c)
    food.d = round(food.d, 2)
    food.e = round(food.e)
    food.k = round(food.k)
    food.omega_3 = round(food.omega_3)

    return food
