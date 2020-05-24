n = int(input())
seq = [x for x in input().split(' ')]

b = []

if n % 2 == 0:
    for j in range(n-1, -1, -2):
        b.append(seq[j])
    for i in range(0, n, 2):
        b.append(seq[i])

else:
    for j in range(n-1, -1, -2):
        b.append(seq[j])
    
    for i in range(1, n, 2):
        b.append(seq[i])

print(' '.join(b))