import os

# path = "E:\\Python\\Advance\\Module\\text.txt"

# if os.path.exists(path):
#     print("That location exists")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a folder")
# else:
#     print("That locatin doesn't exist")


# # closes file automatically
# try:
#     with open("Advance\\Module\\test.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found :(")

# # writing a file
# text = "\nHave a nice day! see you\n"
# with open("Advance\\Module\\test.txt", "a") as file:
#     file.write(text)


# Moving files/folders
source = "Advance\\Module\\copy.txt"
destination = "Advance\\copy.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")