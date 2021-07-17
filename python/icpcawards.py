numberOfTeams = int(input())

winningUniversities = set()
numberOfWinners = 0
for _ in range(numberOfTeams):
    universityName, teamName = input().split()
    if numberOfWinners < 12 and universityName not in winningUniversities:
        numberOfWinners += 1
        winningUniversities.add(universityName)
        print("{} {}".format(universityName, teamName))
