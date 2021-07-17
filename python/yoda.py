value1 = input()
value2 = input()

magnitudeDifference = len(value2) - len(value1)
value1 = max(0, magnitudeDifference) * "0" + value1
value2 = max(0, -magnitudeDifference) * "0" + value2

result1 = ""
result2 = ""
for digit1, digit2 in zip(value1[::-1], value2[::-1]):
    if int(digit1) < int(digit2):
        result2 += digit2
    elif int(digit2) < int(digit1):
        result1 += digit1
    else:
        result1 += digit1
        result2 += digit2

if result1 == "":
    result1 = "YODA"
else:
    result1 = int(result1[::-1])

if result2 == "":
    result2 = "YODA"
else:
    result2 = int(result2[::-1])

print(result1)
print(result2)
