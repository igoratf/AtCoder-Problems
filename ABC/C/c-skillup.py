import itertools

N,M,X = [int(x) for x in input().split(' ')]

bookstore = []
total = float("inf")

for i in range(N):
    book = [int(x) for x in input().split(' ')]
    bookstore.append(book)


for n in range(2**N):
    c_cost = 0
    algos = [0] * M
    
    for i in range(n):
        print('debug aqui')
        print('i ', i)
        print('n ', n)
        print('1<<i ', 1<<i)
        print('1<<i&n ', (1<<i)&n)
        print('\n')
        if (1<<i)&n != 0:
            book = bookstore[i]
            c_cost += book[0]
            
            for x in range(1, M+1):
                algos[x-1] += book[x]
    
    valid = True
    for a in range(M):
        if algos[a] < X:
            valid = False
            break
    
    if valid == True:
        total = min(total, c_cost)

if total == float("inf"):
    print(-1)

else:
    print(total)

