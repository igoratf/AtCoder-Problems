n = int(input())

btns = []
for i in range(n):
    btn = int(input())
    btns.append(btn)


def solve(btns, n):

    attempts = 0
    current = 1

    while True:
        if attempts >= n:
            print("-1")
            return
        
        if current == 2:
            print(attempts)
            return

        current = btns[current-1]
        attempts += 1

solve(btns, n)