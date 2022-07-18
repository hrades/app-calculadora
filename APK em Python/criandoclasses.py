class Pratos:
    def __init__(self, name):
       self.name = name 
    def prato1(self):
        print(f'{self.name} sabe cozinhar lasanha')
        
    def prato2(self):
        print(f'{self.name} sabe cozinhar arroz e feijão')
        
    def prato3(self):
        print(f'{self.name} sabe cozinhar macarronada')
   
pessoa = Pratos('Tadeu')

pessoa.prato1()
pessoa.prato2()
pessoa.prato3()