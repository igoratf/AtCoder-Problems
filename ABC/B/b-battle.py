th, ta, ah, aa = [int(x) for x in input().split(' ')]

index = 0
while (th > 0 and ah > 0):
    if index % 2 == 0:
        ah -= ta
    else:
        th -= aa

    index += 1

if th <= 0:
    print("No")
else:
    print("Yes")