def test(logs):
    numberOfDays = len(logs[0])
    numberOfRecordsTotal = 0
    for log in logs:
        numberOfRecords = log.count("*")
        prefixLength = numberOfDays - numberOfRecords - numberOfRecordsTotal
        suffixLength = numberOfRecordsTotal
        normalizedLog = "." * prefixLength + "*" * numberOfRecords + "." * suffixLength
        numberOfRecordsTotal += numberOfRecords
        print(normalizedLog)


logs = []
isFinished = False
while not isFinished:
    try:
        log = list(input())
    except EOFError:
        isFinished = True

    if isFinished or not log:
        test(logs)
        logs = []
    else:
        logs.append(log)
