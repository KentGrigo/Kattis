seedCost = float(input())
numberOfLawns = int(input())

totalLawnArea = 0
for _ in range(numberOfLawns):
    data = input().split()
    width = float(data[0])
    height = float(data[1])
    
    totalLawnArea += width * height

totalCost = seedCost * totalLawnArea
print(totalCost)