n,m = [int(x) for x in input().split(' ')]

items = [int(a) for a in input().split(' ')]

selected = 0

for i in range(n):
    if items[i] >= ((1/(4*m)) * sum(items)):
        selected += 1

if selected >= m:
    print("Yes")
else:
    print("No")