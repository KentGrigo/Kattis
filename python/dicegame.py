gunnarDice1Low, gunnarDice1High, gunnarDice2Low, gunnarDice2High = list(map(int, input().split()))
emmaDice1Low, emmaDice1High, emmaDice2Low, emmaDice2High = list(map(int, input().split()))

gunnarSum = (gunnarDice1High + gunnarDice1Low) + (gunnarDice2High + gunnarDice2Low)
emmaSum = (emmaDice1High + emmaDice1Low) + (emmaDice2High + emmaDice2Low)

if gunnarSum < emmaSum:
    print("Emma")
elif gunnarSum == emmaSum:
    print("Tie")
else:
    print("Gunnar")
