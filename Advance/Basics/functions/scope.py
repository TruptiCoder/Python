# scope = The region that a variable is recognized.
# A variable is only available from inside the region it is created. 
# A global and locally scoped versions of variable can be created.

# Local -> Enclosing -> Global -> Built-in # order of preference

name = "Trupti" # global scope

def display_name():
    # name = "Code" #local scope
    print(name)

display_name()

print(name)