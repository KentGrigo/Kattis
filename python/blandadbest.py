numberOfOptions = int(input())
options = []
for _ in range(numberOfOptions):
    option = input()
    options.append(option)

if numberOfOptions == 2:
    print("blandad best")
else:
    onlyOption = options[0]
    print(onlyOption)
