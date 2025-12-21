import math

roadLengthInMiles = int(input())
waterGunIntervalLengthInFeet = int(input())

roadLengthInFeet = roadLengthInMiles * 5280
numberOfWaterGuns = math.floor(roadLengthInFeet / waterGunIntervalLengthInFeet)
print(numberOfWaterGuns)
