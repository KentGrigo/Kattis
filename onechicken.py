numberOfPeople, numberOfChickens = list(map(int, input().split()))
leftovers = numberOfChickens - numberOfPeople
if leftovers < -1:
    print("Dr. Chaz needs {} more pieces of chicken!".format(abs(leftovers)))
elif leftovers == -1:
    print("Dr. Chaz needs 1 more piece of chicken!")
elif 1 == leftovers:
    print("Dr. Chaz will have 1 piece of chicken left over!")
elif 1 < leftovers:
    print("Dr. Chaz will have {} pieces of chicken left over!".format(leftovers))
