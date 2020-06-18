n,k = map(int, input().split())

probability = 0
for i in range(1,n+1):
    p = 1/n
    p_head = 1/2
    flips = 0
    prob = p * p_head**flips
    score = i
    
    while score < k:
        flips += 1
        prob = p * p_head**flips
        score = score * 2

    probability += prob


print(probability)


# O(n)?