numberOfElements = int(input())
elements = list(map(lambda element: int(element), input().split()))

min = elements[0]
sortedElements = []
sortedElements.append(str(min))
for element in elements[1:]:
    if min < element:
        min = element
        sortedElements.append(str(min))

print(len(sortedElements))
print(" ".join(sortedElements))
