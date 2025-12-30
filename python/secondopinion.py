import math

totalSeconds = int(input())
hours = math.floor(totalSeconds / 3600)
minutes = math.floor(totalSeconds % 3600 / 60)
seconds = totalSeconds % 60

print(f'{hours} : {minutes} : {seconds}')
