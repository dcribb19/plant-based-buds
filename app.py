# app.py

import calculators
import foods_db
import os
import sqlalchemy
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from nutrient_notes import notes

app = Flask(__name__, static_url_path='/static')
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

nutrients = {
    'macro': ['Protein', 'Fat', 'Omega-3', 'Carbohydrates', 'Fiber'],
    'vitamins': ['A', 'B1 (Thiamine)', 'B2 (Riboflavin)', 'B3 (Niacin)',
                 'B5 (Pantothenic Acid)', 'B6', 'B9 (Folate/Folic Acid)',
                 'B12', 'C', 'D', 'E', 'K'
                 ],
    'minerals': ['Calcium', 'Copper', 'Iron', 'Magnesium', 'Manganese',
                 'Phosphorus', 'Potassium', 'Selenium', 'Zinc'
                 ],
    'vitamin_letters': ['A', 'B1', 'B2', 'B3', 'B5', 'B6', 'B9', 'B12',
                        'C', 'D', 'E', 'K'
                        ]
}

display = {
    'view_1': [
        'Calories', 'Protein (g)', 'Fat (g)', 'Carbs (g)', 'Fiber (g)',
        'Cholesterol (mg)', 'Sodium (mg)', 'Sugar (g)', 'Calcium (mg)',
        'Iron (mg)', 'Potassium (mg)', 'C (mcg)', 'Omega-3 (g)'
    ],
    'view_2': [
        'A (mcg)', 'B1 (mg)', 'B2 (mg)', 'B3 (mg)', 'B5 (mg)', 'B6 (mg)',
        'B9 (mcg)', 'B12 (mcg)', 'C (mg)', 'D (mcg)', 'E (mg)', 'K (mcg)'
    ],
    'view_3': [
        'Calcium (mg)', 'Copper (mg)', 'Iron (mg)', 'Magnesium (mg)',
        'Manganese (mg)', 'Phosphorus (mg)', 'Potassium (mg)',
        'Selenium (mcg)', 'Zinc (mg)'
    ]
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'selector' in request.form:
            return redirect(url_for('nutrient_selector'))
        elif 'calculator' in request.form:
            return redirect(url_for('protein_calculator'))
    return render_template('index.html')


@app.route('/protein_calculator', methods=['GET', 'POST'])
def protein_calculator():
    if request.method == 'POST':
        try:
            weight = float(request.form['weight'])
            units = request.form['units']
            level = request.form['level']

            if units == 'lbs':
                weight = calculators.lbs_to_kg(weight)
            protein = calculators.daily_protein(weight, level)
            return render_template(
                'protein_calculator_results.html', protein=protein
                )
        except ValueError:
            return render_template('protein_calculator.html')
    else:
        return render_template('protein_calculator.html')


@app.route('/protein_calculator_results', methods=['POST'])
def start_over():
    if request.method == 'POST':
        return redirect(url_for('protein_calculator'))


@app.route('/nutrient_selector', methods=['GET', 'POST'])
def nutrient_selector():
    if request.method == 'POST':
        if 'learn more' in request.form:
            try:
                macro = request.form['macro']
                if macro == 'Carbohydrates':
                    macro = 'carbs'
                if macro == 'Omega-3':
                    macro = 'omega_3'
                macro_foods = foods_db.select_foods(macro)
            except KeyError:
                macro = None

            try:
                vitamin = request.form['vitamin']
                vitamin_foods = foods_db.select_foods(vitamin)
            except KeyError:
                vitamin = None

            try:
                mineral = request.form['mineral']
                mineral_foods = foods_db.select_foods(mineral)
            except KeyError:
                mineral = None

            if macro:
                return render_template(
                    'nutrient.html',
                    nutrient=macro,
                    foods=macro_foods,
                    view=1,
                    notes=notes,
                    headers=display['view_1']
                    )
            elif vitamin:
                return render_template(
                    'nutrient.html',
                    nutrient=vitamin,
                    foods=vitamin_foods,
                    view=2,
                    notes=notes,
                    headers=display['view_2']
                    )
            elif mineral:
                return render_template(
                    'nutrient.html',
                    nutrient=mineral,
                    foods=mineral_foods,
                    view=3,
                    notes=notes,
                    headers=display['view_3']
                    )
            else:
                return redirect(url_for('nutrient_selector'))
    return render_template('nutrient_selector.html', nutrients=nutrients)


@app.route('/nutrient_selector/<nutrient>', methods=['GET', 'POST'])
def selection(nutrient):
    if request.method == 'POST':
        if 'back' in request.form:
            return redirect(url_for('nutrient_selector'))

    foods = foods_db.select_foods(nutrient)
    nutrient = nutrient.title()
    if nutrient in nutrients['macro']:
        return render_template(
            'nutrient.html', nutrient=nutrient, foods=foods, view=1,
            notes=notes, headers=display['view_1']
            )
    elif nutrient in nutrients['vitamin_letters']:
        return render_template(
            'nutrient.html', nutrient=nutrient, foods=foods, view=2,
            notes=notes, headers=display['view_2']
            )
    elif nutrient in nutrients['minerals']:
        return render_template(
            'nutrient.html', nutrient=nutrient, foods=foods, view=3,
            notes=notes, headers=display['view_3']
            )
    else:
        return redirect(url_for('nutrient_selector'))


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
@app.errorhandler(500)
@app.errorhandler(sqlalchemy.exc.OperationalError)
def page_not_found(error):
    try:
        return render_template('page_not_found.html')
    except TypeError:
        return render_template('page_not_found.html')


if __name__ == '__main__':
    app.run(debug=True)
