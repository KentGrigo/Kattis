def newMonster(monsters):
    if monsters:
        return monsters.pop()
    else:
        return None

def test():
    _ = input().split()
    godzillas = list(map(lambda strength: int(strength), input().split()))
    mechaGodzillas = list(map(lambda strength: int(strength), input().split()))
    godzillas.sort(reverse=True)
    mechaGodzillas.sort(reverse=True)

    weakestGodzilla = newMonster(godzillas)
    weakestMechaGodzilla = newMonster(mechaGodzillas)
    while weakestGodzilla and weakestMechaGodzilla:
        if weakestGodzilla < weakestMechaGodzilla:
            weakestGodzilla = newMonster(godzillas)
        else:
            weakestMechaGodzilla = newMonster(mechaGodzillas)

    if weakestGodzilla:
        print("Godzilla")
    else:
        print("MechaGodzilla")


numberOfTests = int(input())

for _ in range(numberOfTests):
    _ = input()
    test()
