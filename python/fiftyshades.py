numberOfColors = int(input())

numberOfShades = 0
for _ in range(numberOfColors):
    color = input().lower()
    if "rose" in color or "pink" in color:
        numberOfShades += 1

if numberOfShades == 0:
    print("I must watch Star Wars with my daughter")
else:
    print(numberOfShades)