import os
from pprint import pprint
def read_recipes(file_path='recipes.txt'):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # print(lines)
    i = 0
    while i < len(lines):
        dish_name = lines[i].strip()
        ingr_count = int(lines[i+1])
        # print('ingr count:',ingr_count)
        ingredients = []

        for j in range(ingr_count):
            ingr_info = lines[i+2+j].strip().split('|')
            ingr = {'ingredient_name': ingr_info[0].strip(), 'quantity': int(ingr_info[1].strip()), 'measure': ingr_info[2].strip()}
            ingredients.append(ingr)
        # print(ingredients)
        cook_book[dish_name] = ingredients
        i += ingr_count + 3
    return cook_book

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_recipes()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list
# cook_book = read_recipes()
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# pprint(cook_book,width=100)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2),width=100)