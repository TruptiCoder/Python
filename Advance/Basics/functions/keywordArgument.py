# keyward arguments = arguments preceded by an identifier when we pass them to a function. 
# The order of the arguments doesn't matter, unlike positional arguments. 
# Python knows the names of the arguments that out function receives

def hello(first, middle, last):
    print("Hello " + first + " " + middle + " " + last)

hello(last="Balbudhe", first="Trupti", middle="Yadav")