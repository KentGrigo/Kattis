boxHeight, boxWidth, boxLength, catVolume = list(map(int, input().split()))
boxVolume = boxHeight * boxWidth * boxLength
if catVolume < boxVolume:
    print('SO MUCH SPACE')
elif catVolume == boxVolume:
    print('COZY')
else:
    print('TOO TIGHT')
