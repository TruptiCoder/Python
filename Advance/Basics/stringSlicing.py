# slicing = create a substring by extracting elements from another string 
# indexing[] or slice()
# [start:stop:step]

name = "Trupti Balbudhe"

first_name = name[:6]
last_name = name[7:16]
funcky_name = name[0:16:3]
reversed_name = name[::-1]

# print(first_name)
# print(last_name)
# print(funcky_name)
# print(reversed_name)

website = "https://wikipedia.com"

slice = slice(8, -4)

print(website[slice])