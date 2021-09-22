from pprint import pprint



def prepare_dict(file_name: str) -> dict:
    result: dict = dict()

    with open(file_name, encoding="utf8") as file:
        for line in file:
            dish_name = line.strip()
            number_of_ingredients = int(file.readline())
            ingredient_list = []
            for ingredient in range(number_of_ingredients):
                ingredient_name, quantity, measure = file.readline().split('|')
                ingredient_list.append(
                    {"Ingredient name": ingredient_name, "Quantity": int(quantity), "Measure": measure.split()}
                )
            result[dish_name] = ingredient_list
            file.readline()
    return result


cook_book = prepare_dict("recipes.txt")

# pprint(cook_book)




def get_shop_list_by_dishes(dishname, person_count) -> dict:
    result = dict()
    for i in dishname:
        ingredients = cook_book[i]
        for each in ingredients:
            name = each["Ingredient name"]

            quantity = each["Quantity"]

            measure = each["Measure"][0]

            result[name] ={"Quantity": int(quantity)*person_count, "Measure": measure}
    return result

# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

