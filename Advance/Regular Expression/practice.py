uid = input()
number = 0
j = 0
for i in uid:
    if i.isnumeric():
        number = (number * (10**j)) + int(i)
        j += 1

print(number)
    