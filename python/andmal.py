statement = input()
if 10 <= len(statement):
    counterArgument = statement[:9]
else:
    counterArgument = statement + 'q'

print(counterArgument)
