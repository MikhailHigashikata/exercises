def sequad(n):
    resp = dict()
    
    for i in range(1 ,n + 1):
        resp[i] = i**2
        
    return resp



print(sequad(int(input("Insiria um número: "))))