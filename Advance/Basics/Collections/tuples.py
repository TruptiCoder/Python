# tuple = collection which is ordered and unchnageable used to group together related data

student = ("Trupti", 21, "female")

print(student.count("Trupti"))
print(student.index("female"))

for x in student:
    print(x)

if "Trupti" in student:
    print("Trupti is here!")