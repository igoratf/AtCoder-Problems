n = int(input())

cards = {

}

for s in range(n):
    word = input()
    if word not in cards:
        cards[word] = 1
    else:
        cards[word] += 1

m = int(input())

for r in range(m):
    word = input()
    if word not in cards:
        cards[word] = -1
    else:
        cards[word] -= 1

print(max(max(cards.values()), 0))
