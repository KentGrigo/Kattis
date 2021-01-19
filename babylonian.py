numberOfTests = int(input())
for _ in range(numberOfTests):
    babylonianValues = input().split(",")
    result = 0
    for exponential, babylonianValue in enumerate(babylonianValues[::-1]):
        babylonianNumber = int(babylonianValue) if babylonianValue != "" else 0
        result += babylonianNumber * 60 ** exponential

    print(result)
