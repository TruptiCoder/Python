from Car import Car

car_1 = Car("Chevy", "Corvette", "2021", "blue")
car_2 = Car("Ford", "Mustang", 2022, "Red")

# print(car_2.make)
# print(car_2.model)
# print(car_2.year)
# print(car_2.color)

Car.wheels = 3

print(car_2.wheels)

car_1.wheels = 2
print(car_1.wheels)

car_2.drive()
car_1.stop()
