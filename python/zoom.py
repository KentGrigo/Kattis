_, filterInEvery = list(map(int, input().split()))
numbers = input().split()[filterInEvery-1::filterInEvery]
output = " ".join(numbers)
print(output)
