l,r = map(int, input().split())


def solve(l,r):
    num = float("inf")
    count = 0
    for i in range(l,r):
        for j in range(i+1,r+1):
            if count >= 2019**2:
                print(num)
                return
            
            current = (i*j) % 2019
            if current == 0:
                print(current)
                return
            
            num = min(current,num)
            count += 1
    
    print(num)

solve(l,r)