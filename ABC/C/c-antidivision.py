a,b,c,d = map(int, input().split())

def solve(a,b,c,d):
    x,y = c,d
    def gcd(x,y):
        while y != 0:
            z = y
            y = x % y
            x = z
        return x

    gcd = gcd(c,d)
    lcm = (c*d)//gcd

    mult_b = b // c
    mult_b += b // d
    duplicates = b // lcm
    mult_b -= duplicates

    mult_a = (a-1) // c
    mult_a += (a-1) // d
    duplicates_a = (a-1) // lcm
    mult_a -= duplicates_a

    result = b - (a-1) - (mult_b - mult_a)
    print(result)

solve(a,b,c,d)