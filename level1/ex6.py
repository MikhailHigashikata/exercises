class uptext:
    def __init__(self) -> None:
        self.string: str
        
    def getString(self):
        self.string = input("Insira uma cadeia de caracteres: ")
        
    def printString(self):
        print(self.string.upper())
        
obj = uptext()
obj.getString()
obj.printString()