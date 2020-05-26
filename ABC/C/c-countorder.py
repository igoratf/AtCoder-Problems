from itertools import permutations
N = int(input())

P = [int(x) for x in input().split()]
Q = tuple(map(int, input().split()))

copy = P.copy()
copy.sort()

P = tuple(P)


permuts = list(permutations(copy))

p = 0
q = 0

for i in range(len(permuts)):
    if permuts[i] == P:
        p = i + 1
    if permuts[i] == Q:
        q = i + 1

print(abs(p - q))