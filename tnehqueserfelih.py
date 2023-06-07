class persona:
    def __init__(self, nombre, DNI, direccion):
        self.nombre=nombre
        self.DNI=DNI
        self.direccion=direccion
    def mostrar(self):    
        print("producto:", self.nombre)
        print("precio:", self.DNI)
        print("cantstock:", self.direccion)           
p1=persona    