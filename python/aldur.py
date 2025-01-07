import sys

numberOfFriends = int(input())
minimumAge = sys.maxsize
for _ in range(numberOfFriends):
    age = int(input())
    minimumAge = min(minimumAge, age)

print(minimumAge)
