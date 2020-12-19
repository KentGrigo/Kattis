numberOfBlimps = 5
numberOfCiaBlimps = 0
for blimpNumber in range(1, numberOfBlimps + 1):
    blimp = input()
    if "FBI" in blimp:
        numberOfCiaBlimps += 1
        print(blimpNumber)

if numberOfCiaBlimps == 0:
    print("HE GOT AWAY!")
