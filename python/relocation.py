numberOfCompanies, numberOfRequests = list(map(int, input().split()))
companyNumberToLocation = {}
for index, location in enumerate(list(map(int, input().split()))):
    companyNumber = index + 1
    companyNumberToLocation[companyNumber] = location

for _ in range(numberOfRequests):
    requestType, *data = list(map(int, input().split()))
    if requestType == 1:
        companyNumber = data[0]
        newLocation = data[1]
        companyNumberToLocation[companyNumber] = newLocation
    else:
        companyNumber1 = data[0]
        companyNumber2 = data[1]
        companyLocation1 = companyNumberToLocation[companyNumber1]
        companyLocation2 = companyNumberToLocation[companyNumber2]
        distance = abs(companyLocation1 - companyLocation2)
        print(distance)
