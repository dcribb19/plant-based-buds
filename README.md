# Plant-Based Buds
This is a website built with Python and Flask that aims to help teach users about great sources of plant-based nutrition.

## Motivation
The idea for this project came out of not knowing of any places to quickly search for top plant-based sources of different nutrients that the body needs. There are people that are interested in plant-based diets for a variety of reasons (personal health, animal rights, environmental sustainability, etc.) but do not know where to start. The nutrient selector aims to be that place. All nutrient information was pulled from the USDA FoodData Central API with a focus on whole, minimally processed foods. All displayed foods are vegan. Hopefully this site will inspire users to add more of these foods into their diets or try entirely new foods!

There is also a common misconception that people who eat plant-based diets cannot possibly eat enough protein to survive. So, I also built a protein calculator that provides a recommendation to daily intake based on the users weight and activity level. The protein calculator can then be used with the protein page from the nutrient selector to show that it is possible to consume sufficient levels!

Additionally, I was interested in learning Flask and SQLAlchemy and working more with APIs, and this project seemed ideally suited to take that on.

## Examples
<div align='center'>
    <img width=638 height=211 src=https://github.com/dcribb19/plant-based-buds/blob/master/examples/home.png>
    <img width=402 height=250 src=https://github.com/dcribb19/plant-based-buds/blob/master/examples/nutrient_selector.png><img width=236 height=250 src=https://github.com/dcribb19/plant-based-buds/blob/master/examples/protein_calculator.png>
    <img width=638 height=244 src=https://github.com/dcribb19/plant-based-buds/blob/master/examples/fiber.png>
</div>

## Usage
- Protein Calulator
    - Enter your weight in either lbs or kgs.
    - Select your activity level.
    - Result will be recommended daily intake in g.
- Nutrient Selector
    - Select a nutrient, vitamin, or mineral.
    - Result will be a table of foods containing high levels of the nutrient selected.

## Technologies
- Python 3.8.3
- Flask 1.1.2
- Flask-SQLAlchemy 2.4.4
- requests 2.23.0
- pytest 6.0.1
- sqlalchemy 1.3.18
- gunicorn 20.0.4
- psycopg2 2.8.5

## Credits
- Davis, B., RD, &amp; Melina, V., MS, RD. (2013). [Becoming Vegan Express Edition](https://bookpubco.com/content/becoming-vegan-express-edition). Summertown, TN, TN: Book Publishing Company. 
- U.S. Department of Agriculture, Agricultural Research Service. FoodData Central, 2019. fdc.nal.usda.gov.
- Health Professional Fact Sheets from the [National Institutes of Health, Office of Dietary Supplements](https://ods.od.nih.gov/)
- CSS modified from [Templated](https://templated.co/) Visualize.