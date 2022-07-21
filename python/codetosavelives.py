numberOfTests = int(input())
for _ in range(numberOfTests):
    number1 = int(input().replace(" ", ""))
    number2 = int(input().replace(" ", ""))
    sum = number1 + number2
    output = " ".join(list(str(sum)))
    print(output)
