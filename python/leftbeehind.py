while True:
    numberOfSweetJars, numberOfSourJars = list(map(int, input().split()))
    if numberOfSourJars == 0 and numberOfSweetJars == 0:
        break

    if numberOfSourJars + numberOfSweetJars == 13:
        print("Never speak again.")
    elif numberOfSweetJars < numberOfSourJars:
        print("Left beehind.")
    elif numberOfSweetJars == numberOfSourJars:
        print("Undecided.")
    else:
        print("To the convention.")
