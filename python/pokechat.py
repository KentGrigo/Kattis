text = input()

numbers = input()
indexLength = 3
indexes = []
for indexStart in range(0, len(numbers), indexLength):
    indexEnd = indexStart+indexLength
    number = numbers[indexStart : indexEnd]
    index = int(number) - 1
    indexes.append(index)

message = ""
for index in indexes:
    message += text[index]

print(message)
