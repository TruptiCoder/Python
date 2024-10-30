# sort() method = used with lists
# sort() function = used with iterables

# students = ["Spongbob", "Sandy", "Squidward", "Adam", "Elon"]
# students.sort(reverse=True)

# students = ("Spongbob", "Sandy", "Squidward", "Adam", "Elon")
# sorted_students = sorted(students, reverse=True)

# students = [("Squidwar", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr.Krabs", "C", 78)]

# age = lambda ages:ages[2]
# students.sort(key=age, reverse=True)

students = (("Squidwar", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

age = lambda ages:ages[2]
sorted_students = sorted(students, key=age)

for i in sorted_students:
    print(i)