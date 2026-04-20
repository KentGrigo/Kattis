number = int(input())
if number == 1:
    a = 2
    b = -1
elif number == -999:
    a = -998
    b = -1
else:
    a = number - 1
    b = 1

print("{} {}".format(a, b))
