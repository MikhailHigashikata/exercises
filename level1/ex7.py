import math



def eqcal(seq: list):

    C = 50
    H = 30
    resp = []
    
    for D in seq:
     resp.append(str(int(math.sqrt((2 * C * D)/H))))
     
    return ', '.join(resp)

a = [100, 150, 180]

print(eqcal(a))
     
        