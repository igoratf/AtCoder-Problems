import math

a,b,h,m = [int(x) for x in input().split(' ')]

rad_hour = math.pi * 2 * (h/12 + (m/60)/12)
rad_min = math.pi * 2 * (m/60)

rad = abs(rad_hour - rad_min)

x = (math.pow(a,2) + math.pow(b,2) - (2*a*b*math.cos(rad)))
print(math.sqrt(x))