k = int(input())
a,b = [int(x) for x in input().split(' ')]


def lovegolf(a, b, k):
    for i in range(a, b+1):
        if i % k == 0:
            print("OK")
            return

    print("NG")


lovegolf(a,b,k)