data = input().split()
value1 = int(data[0][::-1])
value2 = int(data[1][::-1])

largestValue = max(value1, value2)
print(largestValue)