numberOfNotes = int(input())
maximumNonfatalBamsePower = 0
for noteNumber in range(numberOfNotes):
    bamsePower, wasFatalOutcome = input().split()
    bamsePower = int(bamsePower)

    if wasFatalOutcome == 'nej':
        maximumNonfatalBamsePower = max(bamsePower, maximumNonfatalBamsePower)

print(maximumNonfatalBamsePower)
