def ex8(x:int, y:int):
    array = []
    
    for i in range(y):
        linha = []
        for j in range(x):
            linha.append(i*j)
            
        array.append(linha)
        
    return array
        
print(ex8(5,3))