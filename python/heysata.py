_ = input()
needle = input()
haystack = input()

wasNeedleFound = False
for letter in haystack:
    if letter == needle:
        wasNeedleFound = True
        break

if (wasNeedleFound):
    print("Unnar fann hana!")
else:
    print("Unnar fann hana ekki!")
