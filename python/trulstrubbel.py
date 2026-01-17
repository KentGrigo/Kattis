points = input()

numberOfPointsForTruls = 0
numberOfPointsForHenry = 0
for point in points:
    if point == 'T':
        numberOfPointsForTruls += 1
    else:
        numberOfPointsForHenry += 1
    
    if (11 <= numberOfPointsForHenry or 11 <= numberOfPointsForTruls) \
       and 2 <= abs(numberOfPointsForTruls - numberOfPointsForHenry):
        numberOfPointsForTruls = 0
        numberOfPointsForHenry = 0

print(f'{numberOfPointsForTruls}-{numberOfPointsForHenry}')
