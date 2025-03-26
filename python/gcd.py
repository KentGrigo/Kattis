import math

number1, number2 = list(map(int, input().split()))
result = math.gcd(number1, number2)
print(result)
