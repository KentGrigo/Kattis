class Population:
    def __init__(self, data):
        self.numberOfLarvae = data[2]
        self.numberOfPupae = data[1]
        self.numberOfMosquitoes = data[0]
        self.larvaToPupaRate = data[4]
        self.pupaToMosquitoRate = data[5]
        self.mosquitoToLarvaRate = data[3]

    def evolve(self):
        newNumberOfLarvae = self.numberOfMosquitoes * self.mosquitoToLarvaRate
        newNumberOfPupae = self.numberOfLarvae // self.larvaToPupaRate
        newNumberOfMosquitoes = self.numberOfPupae // self.pupaToMosquitoRate
        self.numberOfLarvae = newNumberOfLarvae
        self.numberOfPupae = newNumberOfPupae
        self.numberOfMosquitoes = newNumberOfMosquitoes


while True:
    try:
        *data, numberOfWeeks = list(map(int, input().split()))
        population = Population(data)
    except EOFError:
        break

    for _ in range(numberOfWeeks):
        population.evolve()

    print(population.numberOfMosquitoes)

# 1 9 0

# 8 55 144
# 0 8 6
# 0 0 0
