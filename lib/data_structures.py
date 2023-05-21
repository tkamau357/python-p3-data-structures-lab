spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food['name'])
    return names

food_names = get_names(spicy_foods)
print(food_names)


def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if food.get('heat_level', 0) > 5:
            spiciest_foods.append(food)
    return spiciest_foods

spiciest_foods = get_spiciest_foods(spicy_foods)
print(spiciest_foods)


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = "🌶🌶🌶"  # Assuming all spicy foods have the same heat level
        print(f"{food} | Heat Level: {heat_level}")

print_spicy_foods(spicy_foods)


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food
    return None

food = get_spicy_food_by_cuisine(spicy_foods, 'Thai')
print(food)


def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            heat_level = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

print_spiciest_foods(spicy_foods)

def average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    
    total_heat_level = 0
    num_foods = len(spicy_foods)
    
    for food in spicy_foods:
        total_heat_level += food['heat_level']
    
    average_heat = total_heat_level / num_foods
    return int(average_heat)

avg_heat = average_heat_level(spicy_foods)
print(f"Average heat level: {avg_heat}")


def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods

new_food = "Ghost Pepper Nachos, heat_level: 7"

updated_foods = create_spicy_food(spicy_foods, new_food)
print(updated_foods)
