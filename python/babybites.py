numberOfBites = int(input())
counts = input().split()
makesSense = True
for biteNumber, count in enumerate(counts, 1):
    if count == "mumble":
        continue
    else:
        count = int(count)
        if count != biteNumber:
            makesSense = False

if makesSense:
    print("makes sense")
else:
    print("something is fishy")
