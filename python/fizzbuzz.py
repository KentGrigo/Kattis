data = input().split()
fizz = int(data[0])
buzz = int(data[1])
limit = int(data[2])

for value in range(1, limit + 1):
    output = ""
    if value % fizz == 0:
        output += "Fizz"
    if value % buzz == 0:
        output += "Buzz"
    if output == "":
        print(value)
    else:
        print(output)