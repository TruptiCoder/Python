# nested loops = The "inner loop" will finish all of it's iterations before finishing one interation of the "outer loop"

rows = int(input("Enter no. of rows: "))
cols = int(input("Enter no. of columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(cols):
        print(symbol, end=" ")
    print()