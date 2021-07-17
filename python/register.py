registers = map(lambda register: int(register), input().split())
primes = [2, 3, 5, 7, 11, 13, 17, 19]

incrementsLeft = 9699689
value = 0
registerValue = 1
for prime, register in zip(primes, registers):
    value += registerValue * register
    registerValue *= prime
    
print(incrementsLeft - value)
