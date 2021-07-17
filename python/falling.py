import math

height = int(input())
endFrameNumber = math.ceil(math.sqrt(height))
while True:
    startFrameNumberSquared = endFrameNumber ** 2 - height
    startFrameNumber = math.floor(math.sqrt(startFrameNumberSquared))
    hopefullyHeight = endFrameNumber ** 2 - startFrameNumber ** 2
    if startFrameNumber == endFrameNumber - 1 and height < hopefullyHeight:
        print("impossible")
        break
    if height == hopefullyHeight:
        print(startFrameNumber, endFrameNumber)
        break

    endFrameNumber += 1
