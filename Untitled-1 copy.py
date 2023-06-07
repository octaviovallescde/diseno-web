class Producto:
    def __init__(self, nombre, precio,cantstock):
        self.nombre=nombre
        self.precio=precio
        self.cantstock=cantstock
    def mostrar (self):
        print("producto", self.nombre)
        print("precio", self.precio)
        print("cantstock", self.cantstock)
    def agregar ():
        nombre=input("ingrese nombre del producto")
        precio=int("ingrese precio del producto")
        cantstock=int("ingrese la cantidad de stock")   
while True:
     opcion=int(input("menu: \n 1-agregar producto\n 2-mostrar producto\n 3-salida\n"))
     if opcion==2:
         ob1=Producto("pepsi", 469, 15)
         ob2=Producto("felipe", 216735746581, 1)
         ob3=Producto("agua de lel", 250, 10) 
         ob4=Producto("alfajor", 47, 145) 
         ob1.mostrar()
         ob2.mostrar()
         ob3.mostrar()
         ob4.mostrar()
     elif opcion==1:
         ob5=Producto
         ob5.agregar()