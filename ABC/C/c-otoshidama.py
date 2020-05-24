n,y = [int(x) for x in input().split(' ')]

def solve(n,y):
    for a in range(n+1):
        for b in range(n+1):
            c = n - a - b
            if c >= 0:
                current = 10000*a + 5000*b + 1000*c
                if current == y:
                    print(a,b,c)
                    return
    
    print(-1, -1, -1)

solve(n,y)