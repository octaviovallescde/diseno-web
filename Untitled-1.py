class Producto:
    def __init__(self, nombre, precio,cantstock):
        self.nombre=nombre
        self.precio=precio
        self.cantstock=cantstock
    def mostrar (self):
        print("producto", self.nombre)
        print("precio", self.precio)
        print("cantstock", self.cantstock)
while True:
     opcion=int(input("menu: \n 1-agregar producto\n 2-mostrar producto\n 3-salida\n"))
     if opcion==1:
         objeto=input("ingrese un nombre de objeto a crear:")
         id=int(input("ingrese el codigo del producto:"))
         nombre=input("nombre del producto:")
         cantstock=int(input ("ingrese stock: "))
         precio=float(input("ingrese precio"))
         objeto1=Producto(nombre, precio, cantstock)
         while True:
               op=input("¿Desea ingresar otro producto?\n S/N")
               if op=="S" or "s":
                  objeto=input("ingrese un nombre de objeto a crear:")
                  id=int(input("ingrese el codigo del producto:"))
                  nombre=input("nombre del producto:")
                  cantstock=int(input ("ingrese stock: "))
                  precio=float(input("ingrese precio")) 
                  objeto2=Producto(nombre, precio, cantstock)
               elif op=="N" or "n":
                    break
     elif opcion==2:
          objeto1.mostrar()
          objeto2.mostrar() 
     elif opcion==3:
         print("cerrando")
         break
     elif opcion==4:
         def 