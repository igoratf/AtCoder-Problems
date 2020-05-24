n, m = [int(x) for x in input().split(' ')]
conditions = []


for i in range(m):
    s, c = [int(x) for x in input().split(' ')]
    conditions.append([s,c])

def solve(n, m, conditions):
    start = 10**(n-1)
    end = 10**n
    if start == 1:
        start = 0

    for i in range(start, end, 1):
        current = str(i)
        valid = True
        for j in range(m):
            condition = conditions[j]
            if current[condition[0] - 1] != str(condition[1]):
                valid = False
        
        if valid == True:
            print(current)
            return
    
    print(-1)

solve(n, m, conditions)

