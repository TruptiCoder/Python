# print("Hello world!")
# print("This is my first program")

# # Variables in python
# a = 5 # int
# print(a)
# b = 34
# print(b)
# a = 6.2 # float
# print(a)
# c = True # or False --> boolean values
# print(c)
# d = "Trupti" # string
# print(d)
# e = None # None value
# print(e)

# # Type casting
# f = "5"
# print(int(f) + 1)
# g = 5
# print(g + 1)

# # Operators

# # Arithmetic operator
# num1 = 10
# num2 = 3
# print("num1 + num2 is",num1 + num2)
# print("num1 - num2 is",num1 - num2)
# print("num1 * num2 is",num1 * num2)
# print("num1 / num2 is",num1 / num2)
# print("num1 // num2 is",num1 // num2)
# print("num1 ** num2 is",num1 ** num2)
# print("num1 % num2 is",num1 % num2)

# # Assignment operator
# a = 4
# a += 2 # -= , *= , /= , //=, %= , **=
# print(a)

# # Comparision operators
# x = 8
# y = 3
# print(x > y) # < , <= , >= , == , !=, ===

# # Logical operators
# x , y ,z = 8 , 3 , 8
# print(x==z and x<y)
# print(x==z or x<y)
# print(not(x==z))

# # String and String methods
# name = "trupti" # or 'Trupti'
# number = "7"
# print(name)
# print(name[0:3]) # 0 to 2
# print(name.upper())
# print(name.capitalize())
# print(name.count("t"))
# print(number.isnumeric()) # There are many more methods
# # Strings are immutable

# # # User input
# name = input("Enter your name ")
# print(type(name))
# print(name)

# # write a python program to take a number from user as input and add 6 to it
# num = int(input("Enter a number ")) 
# print(type(num))
# print(num + 6) # or int(num)

# a1 = "Trupti"
# a2 = 'Trupti'
# a3 = '''Trupti'''
# print(a1 , a2 , a3)
# a4 = "Trupti" \
#       "Balbudhe"
# print(a4)

# # List and List methods
# l1 = [2 , 3 , 5 , 6 , 1 , "Trupti"]
# print(type(l1))
# print(l1)
# l1.remove("Trupti")
# l1.sort()
# print(l1.count(2))
# print(l1)
# l1.pop()
# l1.append(78)
# # l1.clear()
# print(l1)
# l1.extend([2 , 435, 12, 4])
# print(l1)

# # Tuples and Tuple Methods
# t = (2 , 4 , 34 , 34)
# print(t)
# # Tuples are immutable
# print(t.count(34))
# print(t.index(4))

# # Set and set methods
# a = {2 , 6, 6 , 4, 6 , 23 , 25}
# a2 = {2 , 4 , 6 , 5 , 9}
# print(a)
# print(a2)
# print(a.pop())
# print(a)
# a3 = a.union(a2)
# print(a3)
# b = set() # empty set

# # Dictionary and Methods
# dict1 = {"good": "Something pleasent", "fetch":"to bring", "1":"The number 1"}
# marks = {"Harshit": 34, "Harry": 99, "Trupti": 95, "Smriti": 45, }
# print(dict1["good"])
# print(marks["Trupti"])
# marks["Priyanka"] = 45
# print(marks)

# print(marks.get("Priyanka Chopra")) # doesn't gives error
# print(marks.keys())
# print(marks.values())
# print(marks.items())

# # if-else statement
# age = int(input("Enter your age "))
# if(age >= 18):
#     print("Yes, You can drive")
# elif(age == 1):
#     print("No, You are a kid")
# else:
#     print("No, You can not drive")

# # Match case 
# a = 2
# match a:
#     case 1:
#         print("Case is 1")
#     case 2:
#         print("Case is 2")
#     case 3:
#         print("Case is 3")
#     case _:
#         print("No match found")

# # for loop
# for i in range(1 , 5):
#     print(i)

# print("Printing set....")
# a = [1 , 23 , 45, 67 ,26]
# for item in a:
#     print(item)

# # while loop
# i = 0
# while(i < 10):
#     print(i)
#     i += 1

# while(True):
#     num = int(input("Enter a number "))
#     print(num)
#     if(num == 0):
#         break

# # Functions
# def greetHello(name , end):
#     print("Hello", name , end)
#     print("Hello")
#     print("Hello")
# greetHello("Trupti" , "Thank You")

# def avg(a , b):
#     return a+b/2
# print(avg(3 , 6))

# # Exception Handling
# a = input("Enter your number ")
# try:
#     a = int(a)
#     print(a + 3)
# except Exception as e:
#     print("some error occured: ", e)

# # File I/O

# # Writing to a file
# s = "Trupti is a good girl"
# with open("test.txt" , "w") as f:
#     f.write(s)
# # OR
# fp = open("test.txt" , "w")
# fp.write(s)
# fp.close()

# # Reading to a file
# with open("test.txt" , "r") as f:
#     s = f.read()
# OR
# fp = open("test.txt" , "r")
# s = fp.read()
# fp.close()
# print(s)

# # Appendign to a file
# with open("test.txt" , "a") as f:
#     f.write(" She is so nice")

# # OOPS in python

# class Employee:
#     # Constructor
#     def __init__(self , name , salary):
#         self.name = name
#         self.salary = salary

#     def getSalary(self):
#         return self.salary
    
# rohan = Employee("Rohan" , 3455)
# print(rohan.salary)
# print(rohan.name)

# alice = Employee("Alice" , 500)
# print(alice.salary)
# print(alice.name)