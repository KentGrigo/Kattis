class Group:
    def __init__(self):
        self.sizeOfControlGroup = 0
        self.sizeOfVaccinatedGroup = 0
        self.numberOfControlInfected = 0
        self.numberOfVaccinatedInfected = 0

    def addParticipant(self, isVaccinated, isInfected):
        if isVaccinated:
            if isInfected:
                self.addInfectedVaccinated()
            else:
                self.addUninfectedVaccinated()
        else:
            if isInfected:
                self.addInfectedControl()
            else:
                self.addUninfectedControl()

    def addUninfectedControl(self):
        self.sizeOfControlGroup += 1

    def addInfectedControl(self):
        self.sizeOfControlGroup += 1
        self.numberOfControlInfected += 1

    def addUninfectedVaccinated(self):
        self.sizeOfVaccinatedGroup += 1

    def addInfectedVaccinated(self):
        self.sizeOfVaccinatedGroup += 1
        self.numberOfVaccinatedInfected += 1

    def printEfficacy(self):
        infectionRateForControl = self.numberOfControlInfected / self.sizeOfControlGroup
        infectionRateForVaccinated = self.numberOfVaccinatedInfected / self.sizeOfVaccinatedGroup
        efficacy = (1 - infectionRateForVaccinated / infectionRateForControl) * 100

        if efficacy <= 0:
            print("Not Effective")
        else:
            print(efficacy)

def isYesOrNo(yesOrNo):
    return yesOrNo == "Y"


numberOfParticipants = int(input())
groupA = Group()
groupB = Group()
groupC = Group()
for _ in range(numberOfParticipants):
    participant = list(input())
    isVaccinated = isYesOrNo(participant[0])
    isInfectedWithA = isYesOrNo(participant[1])
    isInfectedWithB = isYesOrNo(participant[2])
    isInfectedWithC = isYesOrNo(participant[3])

    groupA.addParticipant(isVaccinated, isInfectedWithA)
    groupB.addParticipant(isVaccinated, isInfectedWithB)
    groupC.addParticipant(isVaccinated, isInfectedWithC)

groupA.printEfficacy()
groupB.printEfficacy()
groupC.printEfficacy()
