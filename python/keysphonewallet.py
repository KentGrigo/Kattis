mandatoryItems = ["keys", "phone", "wallet"]
numberOfItems = int(input())
for _ in range(numberOfItems):
    item = input()
    if item in mandatoryItems:
        mandatoryItems.remove(item)

if not mandatoryItems:
    print("ready")
else:
    for item in mandatoryItems:
        print(item)
