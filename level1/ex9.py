def sortwords(words:str):
    lword = words.split()
    lword.sort()
    return lword
    
print(sortwords('cachorro dengue jesus maneiro ovni cabide'))