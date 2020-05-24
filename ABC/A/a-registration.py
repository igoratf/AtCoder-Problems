s = input()
t = input()


def registration(s, t):

    first = len(s)
    last = len(t)

    if last - first != 1:
        print("No")
        return

    size = min(first, last)

    for i in range(size):
        if s[i] != t[i]:
            print("No")
            return

    print("Yes")

registration(s, t)
