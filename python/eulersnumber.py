iterations = int(input())
approximationOfEulersConstant = 1.0
denominator = 1
for iteration in range(1, iterations + 1):
    denominator *= iteration
    term = 1 / denominator
    approximationOfEulersConstant += term

print(approximationOfEulersConstant)
