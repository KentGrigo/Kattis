numberOfBeats = int(input())

primes = [2, 3, 5, 7, 11, 13, 17]
for prime in primes:
    if numberOfBeats % prime != 0:
        print(prime)
        break
