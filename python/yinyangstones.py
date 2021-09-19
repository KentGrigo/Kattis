stones = input()
stoneToQuantity = {}
stoneToQuantity["B"] = 0
stoneToQuantity["W"] = 0
for stone in stones:
    stoneToQuantity[stone] += 1

if stoneToQuantity["B"] == stoneToQuantity["W"]:
    print("1")
else:
    print("0")
