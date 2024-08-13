numberOfClassrooms, numberOfBottles = list(map(int, input().split()))
totalNeed = 0
for _ in range(numberOfClassrooms):
    classroomNeed = int(input())
    totalNeed += classroomNeed

if totalNeed <= numberOfBottles:
    print("Jebb")
else:
    print("Neibb")
