import os
import platform

from desafio_1 import (
    productoHeladera,
    productoTelevisor,
    GestionProductos,
)

def limpiar_pantalla():
    ''' Limpiar la pantalla según el sistema operativo'''
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear') 

        
def mostrar_menu():
    print("========== Menú ==========")
    print('1. Agregar Producto')
    print('2. Actualizar productos')
    print('3. Eliminar Producto')
    print('4. Mostrar todos los Productos')
    print('5. salir')
    print('======================================================')

def agregar_producto(gestion):
    try:
        id_producto = input('Ingrese id de el Producto: ')
        nombre = input('Ingrese nombre del Producto: ')
        marca = input('Ingrese marca del Producto: ')
        precio =float(input('Ingrese el precio del Producto: '))
        stock = int(input('Ingrese stock del Producto: '))
        garantia = int(input('Ingrese garantia del Producto: '))
        
        if nombre == 'televisor':
            pantalla_pulgadas = int(input('Ingrese pulgadas de la pantalla: '))
            productos = productoTelevisor(id_producto, nombre, marca,pantalla_pulgadas,precio, stock, garantia)
        elif nombre == 'heladera':
            capacidad = int(input('Ingresar capacida en litors del producto: '))
            productos = productoHeladera(id_producto, nombre, marca,capacidad,precio, stock, garantia)
        else:
            print('Nombre del producto invalido')
            input('Presione enter para continuar...')
            return

        gestion.crear_producto(productos)
        input('Presione enter para continuar...')

    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f'Error inesperado: {e}')    
    input('Presione enter para continuar...')

def actualizar_producto(gestion):
    id_producto = input('Ingrese el id del producto : ')
    atributo = input ('Ingrese atributo que desea actualizar(precio/stock): ')
    if atributo == 'precio':
       precio = float(input('Ingrese Nuevo Precio del Producto: '))
       gestion.actualizar_precio(id_producto, precio)
    elif atributo == 'stock':
       stock = int(input('Ingrese nuevo stock del Producto:'))
       gestion.actualizar_stock(id_producto, stock)
    else :
        print ('opcion no valida') 
        input('Presione enter para continuar...')
        return 
    input('Presione enter para continuar...')

def eliminar_producto(gestion):
    id_producto = input('Ingrese el Id del Producto que desea eliminar: ')
    gestion.eliminar_producto(id_producto)
    input('Presione enter para continuar...')    

def mostrar_todos_los_productos(gestion):
     print('=============== Listado completo de los  Colaboradores ==============')
     for productos in gestion.leer_datos().values():

        if 'capacidad'  in productos:
            print(f"{productos['id_producto']} - {productos['nombre']} - {productos['marca']} - $ {productos['precio']} - {productos['stock']} UN - {productos['garantia']} años - {productos['capacidad']} litros")
        else:
            print(f"{productos['id_producto']} - {productos['nombre']} - {productos ['marca']} - $ {productos['precio']} - {productos['stock']} UN - {productos['garantia']} años - {productos['pantalla_pulgadas']} pulgadas")
     print('=====================================================================') 
     input('Presione enter para continuar...')  

if __name__ == "__main__":
    archivo_productos = 'productos_db.json'
    gestion = GestionProductos(archivo_productos)

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            agregar_producto(gestion)
        
        elif opcion == '2':
            actualizar_producto(gestion)

        elif opcion == '3':
            eliminar_producto(gestion)

        elif opcion == '4':
            mostrar_todos_los_productos(gestion)

        elif opcion == '5':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida (1-6)')     
        
