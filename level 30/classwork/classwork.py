# task 1

car = {
    "brand": "nissan",
    "color": "blue",
    "year": 2000
}

# without function

print(car["brand"])
print(car["color"])
print(car["year"])

# with function

print(car.get("brand"))
print(car.get("year"))
print(car.get("color"))

# task 2

phone = {
    "brand": "realme",
    "color": "black",
    "year": 2021
}

for i in phone.keys():
    print(phone[i])



# task 3

animes = {
    "new": ["jujutsu kaisen", "mushoku tensei", "solo leveling"],
    "old": ["bleach", "one punch man", "death note"],
    "really old": ["dragon ball z", "one piece", "naruto"]
}

# task 4

figures = {
    "wood": "pine",
    "plastic": "rubber",
    "metal": {
        "iron", "bronze", "silver"
    }
}


