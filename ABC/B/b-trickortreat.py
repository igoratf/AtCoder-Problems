n,k = [int(x) for x in input().split(' ')]
 
def solve(n, k):
    snukes = [None] * n
    victims = 0
    
    for i in range(k):
        snacks = int(input())
        snukes_snacks = [int(z) for z in input().split(' ')]
        for j in range(snacks):
            snukes[snukes_snacks[j] - 1] = snukes_snacks[j]
    
    for w in range(n):
        if snukes[w] is None:
            victims += 1
    
    print(victims)
 
solve(n, k)