import math

n,a,b = [int(x) for x in input().split(' ')]

if a == 0:
    print(0)

elif a >= n:
    print(n)

else:
    num_a = (n // (a+b)) * a
    left_repeated = (n % (a+b))
    print(num_a + min(left_repeated, a))
