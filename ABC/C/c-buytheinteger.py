a,b,x = map(int, input().split())

def solve(a,b,x):
    greatest = 0
    if x == 0 or x < (a+b):
        print(0)
        return

    number = findNum(0, 1000000000, x)
    greatest = max(greatest, number)

    print(greatest)

def findNum(left, right, x):
    mid = (left+right)//2
    cost = a*mid + b*len(str(mid))

    if x == cost:
        return mid

    if left == right:
        if x >= cost:
            return mid
        else:
            return mid - 1

    if x > cost:
        return findNum(mid+1, right, x)
    if x < cost:
        return findNum(left, mid-1, x)


solve(a,b,x)