import re
 
diceRoll = input()
pattern = re.compile(r'\d+')
numbers = pattern.findall(diceRoll)
numberOfRolls, diceType, addition = list(map(int, numbers))
min = numberOfRolls * 1 + addition
max = numberOfRolls * diceType + addition
average = (min + max) / 2
print(average)  
