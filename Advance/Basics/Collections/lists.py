# list = used to store multiple items in single variable

food = ["pizza", "burger", "coke", "hamburger", "hotdog"]

food[0] = "sushi"

for i in food:
    print(i)

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0, "cake")
food.sort()
food.clear()

print(food)

# 2d lists = list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice-creame"]

food = [drinks, dinner, dessert]

print(food[0][1])

for i in food:
    for e in i:
        print(e, end=" | ")