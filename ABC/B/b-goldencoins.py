x = int(input())

def solve(x):
    coins = x
    happiness = 0
    t = coins // 500

    happiness += t * 1000
    coins -= t * 500

    h = coins // 5
    happiness += h * 5

    print(happiness)

solve(x)