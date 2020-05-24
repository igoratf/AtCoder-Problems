s = input()

def solve(s):
    maximum = 0
    a = 0
    counting = False
    for i in s:
        if i == "A":
            counting = True
        
        if counting == True:
            a += 1
        
        if i == "Z" and counting == True:
            maximum = a
    
    print(maximum)
        

solve(s)