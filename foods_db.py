# foods_db.py
# Create database of foods and other db-related functions.

from sqlalchemy import Table, Column, MetaData, create_engine
from sqlalchemy import Integer, Float, String
from sqlalchemy.sql import text
from sqlalchemy.sql.schema import ForeignKey
from food_data_central import get_multiple_foods

engine = create_engine('sqlite:///foods.db')

metadata = MetaData()

foods = Table('foods', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String, nullable=False),
              Column('protein', Integer, default=0),
              Column('fat', Integer, default=0),
              Column('carbs', Integer, default=0),
              Column('calories', Integer, nullable=False),
              Column('sugar', Integer, default=0),
              Column('fiber', Integer, default=0),
              Column('calcium', Integer, default=0),
              Column('iron', Float, default=0),
              Column('magnesium', Float, default=0),
              Column('phosphorus', Integer, default=0),
              Column('potassium', Integer, default=0),
              Column('sodium', Integer, default=0),
              Column('zinc', Float, default=0),
              Column('chromium', Float, default=0),
              Column('copper', Float, default=0),
              Column('iodine', Float, default=0),
              Column('manganese', Float, default=0),
              Column('selenium', Float, default=0),
              Column('added_sugar', Integer, default=0),
              Column('cholesterol', Integer, default=0),
              Column('trans_fat', Integer, default=0),
              Column('saturated_fat', Integer, default=0),
              Column('mono_fat', Integer, default=0),
              Column('poly_fat', Integer, default=0),
              Column('a', Integer, default=0),
              Column('b1', Float, default=0),
              Column('b2', Float, default=0),
              Column('b3', Float, default=0),
              Column('b5', Float, default=0),
              Column('b6', Float, default=0),
              Column('b7', Float, default=0),
              Column('b9', Integer, default=0),
              Column('b12', Float, default=0),
              Column('c', Integer, default=0),
              Column('d', Integer, default=0),
              Column('e', Integer, default=0),
              Column('k', Integer, default=0),
              Column('omega_3', Integer, default=0),
              )

units = Table('units', metadata,
              Column('id', Integer),
              Column('name', String)
              )

nutrients = Table('nutrients', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String),
                  Column('unit_id', Integer, ForeignKey('units.id')),
                  Column('notes', String)
                  )


def insert_foods(list_of_foods: list):
    '''
    Request a list of foods and then insert into Table.
    '''
    # Request foods from FoodData Central API.
    request = get_multiple_foods(list_of_foods)
    # Connect to database.
    conn = engine.connect()
    # Select table to insert data.
    ins = foods.insert()

    for item in request:
        # Execute insert statement for each food item requested.
        conn.execute(ins,
                     id=item.id,
                     name=item.name,
                     protein=item.protein,
                     fat=item.fat,
                     carbs=item.carbs,
                     calories=item.calories,
                     sugar=item.sugar,
                     fiber=item.fiber,
                     calcium=item.calcium,
                     iron=item.iron,
                     magnesium=item.magnesium,
                     phosphorus=item.phosphorus,
                     potassium=item.potassium,
                     sodium=item.sodium,
                     zinc=item.zinc,
                     chromium=item.chromium,
                     copper=item.copper,
                     iodine=item.iodine,
                     manganese=item.manganese,
                     selenium=item.selenium,
                     added_sugar=item.added_sugar,
                     cholesterol=item.cholesterol,
                     trans_fat=item.trans_fat,
                     saturated_fat=item.saturated_fat,
                     mono_fat=item.mono_fat,
                     poly_fat=item.poly_fat,
                     a=item.a,
                     b1=item.b1,
                     b2=item.b2,
                     b3=item.b3,
                     b5=item.b5,
                     b6=item.b6,
                     b7=item.b7,
                     b9=item.b9,
                     b12=item.b12,
                     c=item.c,
                     d=item.d,
                     e=item.e,
                     k=item.k,
                     omega_3=item.omega_3
                     )
    conn.close()


def select_foods(nutrient: str):
    '''
    Return Top-20 foods rich in the passed nutrient.
    '''
    top_20 = []
    conn = engine.connect()
    s = text(
        "SELECT * FROM foods WHERE {} > 0 ORDER BY {} DESC LIMIT 20".format(
            nutrient, nutrient
            )
    )
    result = conn.execute(s)
    for row in result:
        top_20.append(row)
    conn.close()
    return top_20
