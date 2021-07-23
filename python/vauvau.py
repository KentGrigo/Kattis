dog1AggressionTime, dog1CalmTime, dog2AggressionTime, dog2CalmTime = list(map(int, input().split()))
workerArrivalTimes = list(map(int, input().split()))
for workerArrivalTime in workerArrivalTimes:
    dog1CycleTime = dog1AggressionTime + dog1CalmTime
    dog2CycleTime = dog2AggressionTime + dog2CalmTime
    workerArrivalTimeInCycle1 = workerArrivalTime % dog1CycleTime
    workerArrivalTimeInCycle2 = workerArrivalTime % dog2CycleTime
    numberOfAggresiveDogs = 0
    if 0 < workerArrivalTimeInCycle1 <= dog1AggressionTime:
        numberOfAggresiveDogs += 1

    if 0 < workerArrivalTimeInCycle2 <= dog2AggressionTime:
        numberOfAggresiveDogs += 1

    output = {
        0: "none",
        1: "one",
        2: "both",
    }[numberOfAggresiveDogs]
    print(output)
