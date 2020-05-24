n,m = [int(x) for x in input().split(' ')]

assignments = [int(a) for a in input().split(' ')]
total_a = sum(assignments)
if total_a <= n:
    print(n-total_a)
else:
    print(-1)