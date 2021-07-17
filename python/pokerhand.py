cards = input().split()

ranks = {}
for card in cards:
    rank = card[0]
    ranks[rank] = ranks.get(rank, 0) + 1

mostOccurringRank = max(ranks, key = ranks.get)
handStrengh = ranks[mostOccurringRank]
print(handStrengh)
