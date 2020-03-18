import collections

cards = collections.deque([i+1 for i in range(int(input()))])
while len(cards) != 1:
    del cards[0]
    tmp = cards[0]
    del cards[0]
    cards.append(tmp)
print(*cards)