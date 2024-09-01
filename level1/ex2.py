#Minha solução:

def fatorial(num):
    resp = 1

    for i in range(1, num + 1):
        resp *= i
        
    return resp
    
#Solução recursiva

def fator(num):
    if num == 0:
        return 1
    
    return fator(num-1) * num


if __name__ == "__main__":

    num = int(input("Insira um número aqui: "))

    print(fatorial(num))
    print(fator(num))