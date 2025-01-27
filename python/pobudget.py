numberOfStatements = int(input())
sum = 0
for _ in range(numberOfStatements):
    input() # Title, not needed
    value = int(input())
    sum += value

if sum < 0:
    print("Nekad")
elif 0 < sum:
    print("Usch, vinst")
else:
    print("Lagom")
