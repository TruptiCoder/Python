# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The " + animal + " jumped over the " + item)

print("The {} jumped over the {}".format(animal, item))

# positional arguments
print("The {1} jumped over the {0}".format(animal, item))

# keyward argument
print("The {a} jumped over the {b}".format(a = "dog", b = "wall"))

text = "The {} jumped over the {}"
print(text.format(animal, item))

name = "Bro"

print("hello, my name is {} Nice to meet you".format(name))

# padding
print("hello, my name is {:10} Nice to meet you".format(name))

# alignment
print("hello, my name is {:<10} Nice to meet you".format(name))
print("hello, my name is {:>10} Nice to meet you".format(name))
print("hello, my name is {:^10} Nice to meet you".format(name))