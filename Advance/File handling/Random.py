import random

x = random.randint(1, 6)
y = random.random()

print(x)
print(y)

# Rock , Paper and Scissor

myList = ["Rock", "Paper", "Scissor"]
z = random.choice(myList)
print(z)

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)