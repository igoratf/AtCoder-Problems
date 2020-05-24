a,b,c,k = [int(x) for x in input().split(' ')]


def verify_sum(a,b,c,k):
    if k == a:
        print(a)
        return

    num_cards = a + b
    if k <= a:
        print(k)
    elif k > num_cards:
        print(a - (k-num_cards))
    else:
        print(a)

verify_sum(a,b,c,k)