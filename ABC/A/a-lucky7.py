n = input()

def lucky(n):
    for i in n:
        if i == "7":
            print("Yes")
            return
    
    print("No")

lucky(n)
