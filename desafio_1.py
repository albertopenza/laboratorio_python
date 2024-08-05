#Desafío 1: Sistema de Gestión de Productos
#Objetivo: Desarrollar un sistema para manejar productos en un inventario.

#Requisitos:

#Crear una clase base Producto con atributos como nombre, precio, cantidad en stock, etc.
#Definir al menos 2 clases derivadas para diferentes categorías de productos (por ejemplo, ProductoElectronico, ProductoAlimenticio) con atributos y métodos específicos.
#Implementar operaciones CRUD para gestionar productos del inventario.
#Manejar errores con bloques try-except para validar entradas y gestionar excepciones.
#Persistir los datos en archivo JSON."

import json
class productos:
    def __init__(self,id_producto,nombre,marca,precio,stock,garantia):
        self.__id_producto = id_producto
        self.__nombre = nombre.upper() 
        self.__marca = marca.upper()
        self.__precio = self.validar_precio(precio)
        self.__stock = stock 
        self.__garantia = garantia

    @property
    def id_producto(self):
        return self.__id_producto
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def marca(self):
        return self.__marca

    @property
    def precio(self):
        return self.__precio
    
    @property
    def stock(self):
        return self.__stock
    
    @property
    def garantia(self):
        return self.__garantia
    
    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = self.validar_precio(nuevo_precio)

    def validar_precio(self, precio):
        try:
            precio_num = float(precio)
            if precio_num <= 0:
                raise ValueError("El precio debe ser numérico positivo.")
            return precio_num
        except ValueError:
            raise ValueError("El precio debe ser un número válido.")
    
   
    def to_dict(self):
        return{
            'id_producto': self.__id_producto,
            'nombre': self.__nombre,
            'marca':self.__marca,
            'precio': self.__precio,
            'stock' : self.__stock,
            'garantia':self.__garantia
        }

    def __str__(self):
        return f'{self.__id_producto},{self.__nombre},{self.__marca},{self.__precio}'
      

class productoTelevisor(productos):
    def __init__ (self,id_producto,nombre,marca,pantalla_pulgadas,precio,stock,garantia):
        super().__init__(id_producto,nombre,marca,precio,stock,garantia)
        self.__pantalla_pulgadas = pantalla_pulgadas

    @property
    def pantalla_pulgadas(self):
        return self.__pantalla_pulgadas

    def to_dict(self):
        data = super().to_dict()
        data ["pantalla_pulgadas"]= self.__pantalla_pulgadas
        return data
        

    def __str__(self): 
        return f'{super( ).__str__()} - pantall_pulgadas {self.__pantalla_pulgadas}'

      
class productoHeladera(productos):
    def __init__ (self,id_producto,nombre,marca,capacidad_litros,precio,stock,garantia):
        super().__init__(id_producto,nombre,marca,precio,stock,garantia)
        self.__capacidad_litros = capacidad_litros

    @property
    def capacidad(self):
        return self.__capacidad_litros   

    def to_dict(self):
        data = super().to_dict()
        data ["capacidad"]= self.__capacidad_litros
        return data
        

    def __str__(self):
        return f'{super().__str__()} - capacidad {self.__capacidad_litros}' 

class GestionProductos:
    def __init__(self, archivo):
        self.archivo = archivo

    def leer_datos(self):
        try:
            with open(self.archivo, 'r') as file:
                datos = json.load(file)
        except FileNotFoundError:
            return {}
        except Exception as error:
            raise Exception(f'Error al leer datos del archivo: {error}')
        else:
            return datos

    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w') as file:
                json.dump(datos, file, indent=4)
        except IOError as error:
            print(f'Error al intentar guardar los datos en {self.archivo}: {error}')
        except Exception as error:
            print(f'Error inesperado: {error}')

    def crear_producto(self, productos):
        try:
            datos = self.leer_datos()
            id_producto = productos.id_producto
            if not str(id_producto) in datos.keys():
                datos[id_producto] = productos.to_dict()
                self.guardar_datos(datos)
                print(f"El producto {productos.nombre} se agrego correctamente.")
            else:
                print(f"el pructo id {id_producto} ya existe.")
        except Exception as error:
            print(f'Error al agregar el producto: {error}')

    def actualizar_precio(self, id_producto, nuevo_precio):
        try:
            datos = self.leer_datos()
            if str(id_producto) in datos.keys():
                 datos[id_producto]['precio'] = nuevo_precio
                 self.guardar_datos(datos)
                 print(f'Se actualizo precio del producto con Id:{id_producto}')
            else:
                print(f'No se encontró producto con Id:{id_producto}')
        except Exception as e:
            print(f'Error al actualizar el precio: {e}')

    def actualizar_stock(self, id_producto, nuevo_stock):
        try:
            datos = self.leer_datos()
            if str(id_producto) in datos.keys():
                 datos[id_producto]['stock'] = nuevo_stock
                 self.guardar_datos(datos)
                 print(f'Se actualizo stock del producto con Id:{id_producto}')
            else:
                print(f'No se encontró producto con Id:{id_producto}')
        except Exception as e:
            print(f'Error al actualizar el stock: {e}')

    def eliminar_producto(self, id_producto):
        try:
            datos = self.leer_datos()
            if str(id_producto) in datos.keys():
                 del datos[id_producto]
                 self.guardar_datos(datos)
                 print(f'El producto Id:{id_producto} se elimino correctamente')
            else:
                print(f'No se encontró Id:{id_producto}')
        except Exception as e:
            print(f'Error al eliminar producto: {e}')    


























