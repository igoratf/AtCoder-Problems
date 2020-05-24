lista = [1,2,3,4]

def brute(pos, sub):
    if pos == len(lista):
     print(pos)
    else:
        brute(pos + 1, sub)
        brute(pos + 1, sub + [lista[pos]])

brute(0, [1,2,3,4])