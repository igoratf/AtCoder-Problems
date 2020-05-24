n,m = [int(x) for x in input().split(' ')]

info = {
    
}

for i in range(m):
    p,s = [x for x in input().split(' ')]
    if p not in info:
        if s == "WA":
            info[p] = [0, 1]
        elif s == "AC":
            info[p] = [1,0]
    else:
        if s == "WA":
            if info[p][0] == 0:
                info[p][1] += 1
        elif s == "AC":
            if info[p][0] == 0:
                info[p][0] = 1
    
ac = 0
wa = 0

for a in info.values():
    ac += a[0]
    if a[0] > 0:
        wa += a[1]

print(ac, wa)


