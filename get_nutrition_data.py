import requests
import pandas as pd


def get_nutrition(food_name):
    nutrition_data = pd.DataFrame(columns=['name', 'protein', 'calcium', 'fat', 'carbohydrates', 'vitamins'])
    for name in food_name:
        url = "https://api.nal.usda.gov/fdc/v1/foods/search?api_key=d4D6dSOc81pTAOY2gsNZ0YhjkMlhStLJRoII5SJu&query=" + name
        response = requests.get(url)
        data = response.json()
        flatten_json = pd.json_normalize(data["foods"])
        first_food = flatten_json.iloc[0]
        first_food_nutrition_list = first_food.foodNutrients
        for item in first_food_nutrition_list:
            if item['nutrientNumber'] == "203":
                protein = item['value']
                continue
            if item['nutrientNumber'] == "301":
                calcium = item['value']
                continue
            if item['nutrientNumber'] == "204":
                fat = item['value']
                continue
            if item['nutrientNumber'] == "205":
                carbs = item['value']
                continue
            if item['nutrientNumber'] == "318":
                vitamin_a = item['value']
                continue
            if item['nutrientNumber'] == "401":
                vitamin_c = item['value']
                continue

        vitamins = float(vitamin_a) + float(vitamin_c)
        print(name)
        nutrition_data = nutrition_data.append({
            'name': name,
            'protein': protein,
            'calcium': calcium / 1000,
            'fat': fat,
            'carbohydrates': carbs,
            'vitamins': vitamins / 1000
        }, ignore_index=True)

    return nutrition_data


nutrition101 = get_nutrition(['apple pie',
                              'baby back ribs',
                              'baklava',
                              'beef carpaccio',
                              'beef tartare',
                              'beet salad',
                              'beignets',
                              'bibimbap',
                              'bread pudding',
                              'breakfast burrito',
                              'bruschetta',
                              'caesar salad',
                              'cannoli',
                              'caprese salad',
                              'carrot cake',
                              'ceviche',
                              'cheese plate',
                              'cheesecake',
                              'chicken curry',
                              'chicken quesadilla',
                              'chicken wings',
                              'chocolate cake',
                              'chocolate mousse',
                              'churros',
                              'clam chowder',
                              'club sandwich',
                              'crab cakes',
                              'creme brulee',
                              'croque madame',
                              'cup cakes',
                              'deviled eggs',
                              'donuts',
                              'dumplings',
                              'edamame',
                              'eggs benedict',
                              'escargots',
                              'falafel',
                              'filet mignon',
                              'fish and_chips',
                              'foie gras',
                              'french fries',
                              'french onion soup',
                              'french toast',
                              'fried calamari',
                              'fried rice',
                              'frozen yogurt',
                              'garlic bread',
                              'gnocchi',
                              'greek salad',
                              'grilled cheese sandwich',
                              'grilled salmon',
                              'guacamole',
                              'gyoza',
                              'hamburger',
                              'hot and sour soup',
                              'hot dog',
                              'huevos rancheros',
                              'hummus',
                              'ice cream',
                              'lasagna',
                              'lobster bisque',
                              'lobster roll sandwich',
                              'macaroni and cheese',
                              'macarons',
                              'miso soup',
                              'mussels',
                              'nachos',
                              'omelette',
                              'onion rings',
                              'oysters',
                              'pad thai',
                              'paella',
                              'pancakes',
                              'panna cotta',
                              'peking duck',
                              'pho',
                              'pizza',
                              'pork chop',
                              'poutine',
                              'prime rib',
                              'pulled pork sandwich',
                              'ramen',
                              'ravioli',
                              'red velvet cake',
                              'risotto',
                              'samosa',
                              'sashimi',
                              'scallops',
                              'seaweed salad',
                              'shrimp and grits',
                              'spaghetti bolognese',
                              'spaghetti carbonara',
                              'spring rolls',
                              'steak',
                              'strawberry shortcake',
                              'sushi',
                              'tacos',
                              'octopus balls',
                              'tiramisu',
                              'tuna tartare',
                              'waffles']
                             )
nutrition101 = nutrition101.reset_index(drop=True)
nutrition101.to_csv("nutrition101.csv")
