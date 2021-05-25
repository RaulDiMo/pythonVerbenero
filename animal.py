#Crear una clase animal con atributo vivo que es boolean, un método esta_vivo que devuelve boolean y 
#una clase gato que además de lo que tiene animal tiene lo métodos correr, dormir, ronrronear y maullar
#Los métodos del gatos devolverían un string, por ejemplo, dormir devolvería zzzz, ronronear rrrrr, y maullar miau


class Animal():
    def __init__(self):
        self.isVivo = True
 
    def vivo(self):
       print("Está vivo")
       return self.isVivo
 
class Gato(Animal):
          
    
 
    def dormir(self):
        print("zzzz")
 
    def ronrronear(self):
       print("rrrrr")
 
    def maullar(self):
        print("Miau")
    
 
pussycat = Gato()
print(pussycat.vivo())
pussycat.dormir()
pussycat.ronrronear()
pussycat.maullar()







   