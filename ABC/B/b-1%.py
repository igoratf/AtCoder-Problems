inp = int(input())

def solve(value):
    current = 100
    for i in range(1000000):
        current = int(current * (1.01**1))
        if current >= value:
            print(i+1)
            return

solve(inp)