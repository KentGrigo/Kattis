numberOfTests = int(input())

for _ in range(numberOfTests):
    input() # blank line
    numberOfChildren = int(input())
    sum = 0
    for _ in range(numberOfChildren):
        sum += int(input())

    isDivisible = sum % numberOfChildren == 0
    if isDivisible:
        print("YES")
    else:
        print("NO")
