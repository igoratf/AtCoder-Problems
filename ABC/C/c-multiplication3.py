nums = [x for x in input().split()]
a,b = int(nums[0]), float(nums[1])
b = round(b*100)
res = (a*b) // 100
print(res)