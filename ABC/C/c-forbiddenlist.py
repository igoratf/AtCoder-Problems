x,n = map(int, input().split())
seq = [int(x) for x in input().split()]

def solve(x, n, seq):
    if n == 0:
        print(x)
        return

    lower = x - 1
    higher = x + 1

    seq_set = set()

    for i in range(n):
        current = seq[i]
        seq_set.add(current)
    
    
    while lower in seq_set and lower > 0:
        lower -= 1
    
    while higher in seq_set and higher <= 100:
        higher += 1
    
    lower_diff = abs(lower - x)
    higher_diff = abs(higher - x)

    if lower_diff and higher_diff > 1 and x not in seq_set:
        print(x)
    elif lower_diff <= higher_diff:
        print(lower)
    elif higher not in seq_set:
        print(higher)
    else:
        print(x)
    

solve(x,n,seq)
    

