firstName, lastName = input().split()

if firstName[-1] in ["a", "e", "i", "o", "u"]:
    print(firstName[:-1] + "ex" + lastName)
elif firstName[-2:] == "ex":
    print(firstName + lastName)
else:
    print(firstName + "ex" + lastName)
