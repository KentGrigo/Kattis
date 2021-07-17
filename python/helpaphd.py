numberOfTests = int(input())
for _ in range(numberOfTests):
    expression = input()
    if expression == "P=NP":
        print("skipped")
    else:
        value1, value2 = list(map(int, expression.split("+")))
        print(value1 + value2)
