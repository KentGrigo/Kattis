import statistics

while True:
    try:
        data = input().split()
    except EOFError:
        break

    name = []
    heartRates = []
    for entry in data:
        try:
            heartRate = float(entry)
            heartRates.append(heartRate)
        except ValueError:
            name.append(entry)

    name = " ".join(name)
    if heartRates:
        averageHeartRate = statistics.mean(heartRates)
    else:
        averageHeartRate = 0.0

    print("{} {}".format(averageHeartRate, name))
