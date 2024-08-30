# task 2

car = {
    "model": "nissan",
    "color": "blue",
    "release": 1998
}

for key, value in car.items():
    print(f"Key: {key}, Value: {value}")

# task 3

cars = [
    {
        "model": "Toyota Corolla",
        "color": "Red",
        "release": 2010
    },
    {
        "model": "Honda Civic",
        "color": "Black",
        "release": 2015
    },
    {
        "model": "Ford Mustang",
        "color": "Blue",
        "release": 2020
    }
]


for i, car in enumerate(cars, start=1):
    print(f"Car {i}:")
    print(f"  Model: {car['model']}")
    print(f"  Color: {car['color']}")
    print(f"  Release Year: {car['release']}")
    print()