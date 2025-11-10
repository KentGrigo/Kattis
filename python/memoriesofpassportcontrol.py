import math

numberOfStampsPerTrip, numberOfStamps = list(map(int, input().split()))
numberOfMultistampTrips = math.floor(numberOfStamps / numberOfStampsPerTrip)
numberOfSinglestampTrips = numberOfStamps - (numberOfMultistampTrips * numberOfStampsPerTrip)
minimumNumberOfTrips = numberOfSinglestampTrips + numberOfMultistampTrips
print(minimumNumberOfTrips)
