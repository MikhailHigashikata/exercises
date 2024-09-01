s = input()
valor = {'uppercase':0, 'lowercase':0}


for c in s:
    if c.isupper():
        valor['uppercase'] += 1
        
    elif c.islower():
        valor['lowercase'] += 1

print(valor)
