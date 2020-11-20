numberOfRestaurants = int(input())
output = "Anywhere is fine I guess"
for _ in range(numberOfRestaurants):
    numberOfMenuItems = int(input())
    restaurantName = input()
    hasPeaSoup = False
    hasPancakes = False
    for _ in range(numberOfMenuItems):
        item = input()
        if item == "pea soup":
            hasPeaSoup = True
        if item == "pancakes":
            hasPancakes = True
    if hasPeaSoup and hasPancakes:
        output = restaurantName
        break

print(output)
