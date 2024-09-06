# variable = a container for a value. Behaves as the value that it contains

first_name = "Trupti"
last_name = "Balbudhe"
full_name = first_name + " " + last_name
# print(type(full_name))
print("Hello " + full_name)

age = 21
age += 1
# print(type(age))
# print("My age is " + age) #error
print("Your age is " + str(age))
# or
print("Your age is ", age)

height = 250.5
# print(type(height))
print("Your height is " + str(height) + "cm")

human = True
# print(type(human))
print("I am a human: " + str(human))