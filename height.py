def swap(array, index1, index2):
    value1 = array[index1]
    value2 = array[index2]
    array[index1] = value2
    array[index2] = value1

def move(array, index1, index2):
    for index in reversed(range(index2, index1)):
        swap(array, index, index + 1)

def findFirstTallerPerson(index1, height1):
    for index2 in range(index1):
        height2 = heights[index2]
        if height1 < height2:
            return (index2, height2)
    
    return None

def test(heights):
    stepBacks = 0
    for index1 in range(len(heights)):
        height1 = heights[index1]
        firstTallerPerson = findFirstTallerPerson(index1, height1)
        if firstTallerPerson == None:
            continue

        index2, _ = firstTallerPerson
        move(heights, index1, index2)
        stepBacks += (index1 - index2)

    return stepBacks


numberOfTests = int(input())
for _ in range(numberOfTests):
    data = list(map(lambda value: int(value), input().split()))
    testNumber = data[0]
    heights = data[1:]

    numberOfStepBacks = test(heights)
    print("{} {}".format(testNumber, numberOfStepBacks))


