numberOfCases = int(input())

for i in range(numberOfCases):
    data = input().split()
    expectedWithoutAdvertisements = int(data[0])
    expectedWithAdvertisements = int(data[1])
    costOfAdvertisements = int(data[2])
    
    profitWithAdvertisements = expectedWithAdvertisements - costOfAdvertisements
    profitWithoutAdvertisements = expectedWithoutAdvertisements

    if profitWithoutAdvertisements < profitWithAdvertisements:
        print("advertise")
    elif profitWithoutAdvertisements == profitWithAdvertisements:
        print("does not matter")
    else:
        print("do not advertise")
