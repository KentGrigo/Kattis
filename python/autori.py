names = input().split("-")

abbreviation = ""
for name in names:
    abbreviation += name[0]

print(abbreviation)
