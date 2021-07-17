class Nutrient:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __repr__(self):
        return "{} {}".format(self.value, self.unit)

class Nutrients:
    def __init__(self, nutrients):
        self.fat = nutrients[0]
        self.protein = nutrients[1]
        self.sugar = nutrients[2]
        self.starch = nutrients[3]
        self.alcohol = nutrients[4]

    def normalize(self):
        self._normalizeWeightToEnergy()
        self._normalizeRelativeToAbsoluteEnergy()

    def _normalizeWeightToEnergy(self):
        if self.fat.unit == "g":
            self.fat = Nutrient(self.fat.value * 9, "C")
        if self.protein.unit == "g":
            self.protein = Nutrient(self.protein.value * 4, "C")
        if self.sugar.unit == "g":
            self.sugar = Nutrient(self.sugar.value * 4, "C")
        if self.starch.unit == "g":
            self.starch = Nutrient(self.starch.value * 4, "C")
        if self.alcohol.unit == "g":
            self.alcohol = Nutrient(self.alcohol.value * 7, "C")

    def _normalizeRelativeToAbsoluteEnergy(self):
        ratio = 0
        amountOfCalories = 0
        if self.fat.unit == "%":
            ratio += self.fat.value
        else:
            amountOfCalories += self.fat.value

        if self.protein.unit == "%":
            ratio += self.protein.value
        else:
            amountOfCalories += self.protein.value

        if self.sugar.unit == "%":
            ratio += self.sugar.value
        else:
            amountOfCalories += self.sugar.value

        if self.starch.unit == "%":
            ratio += self.starch.value
        else:
            amountOfCalories += self.starch.value

        if self.alcohol.unit == "%":
            ratio += self.alcohol.value
        else:
            amountOfCalories += self.alcohol.value

        otherRatio = 100 - ratio
        caloriesPercent = amountOfCalories / otherRatio

        if self.fat.unit == "%":
            self.fat = Nutrient(self.fat.value * caloriesPercent, "C")

        if self.protein.unit == "%":
            self.protein = Nutrient(self.protein.value * caloriesPercent, "C")

        if self.sugar.unit == "%":
            self.sugar = Nutrient(self.sugar.value * caloriesPercent, "C")

        if self.starch.unit == "%":
            self.starch = Nutrient(self.starch.value * caloriesPercent, "C")

        if self.alcohol.unit == "%":
            self.alcohol = Nutrient(self.alcohol.value * caloriesPercent, "C")

    def totalCalories(self):
        return self.fat.value + self.protein.value + self.sugar.value + self.starch.value + self.alcohol.value

    def __repr__(self):
        return "Fat: {}. Protein: {}. Sugar: {}. Starch: {}. Alcohol: {}.".format(self.fat, self.protein, self.sugar, self.starch, self.alcohol)

def test(entries):
    totalCalories = 0
    totalFatCalories = 0
    for entry in entries:
        entry = entry.split()
        nutrients = []
        for nutrient in entry:
            value = int(nutrient[:-1])
            unit = nutrient[-1]
            nutrient = Nutrient(value, unit)
            nutrients.append(nutrient)

        nutrients = Nutrients(nutrients)
        nutrients.normalize()
        totalCalories += nutrients.totalCalories()
        totalFatCalories += nutrients.fat.value

    fatCaloriesRatio = int(round(totalFatCalories / totalCalories * 100))
    print("{}%".format(fatCaloriesRatio))


entries = []
while True:
    entry = input()
    if (entry == "-"):
        if entries:
            test(entries)
            entries = []
        else:
            break
    else:
        entries.append(entry)
