
from typing import Dict
productos = {
    "XML018262": {"nombre": "MELON", "precio": 3000},
    "XML018263": {"nombre": "SANDIA", "precio": 2500},
    "XML018264": {"nombre": "MANZANA", "precio": 1200},
    "XML018265": {"nombre": "NARANJA", "precio": 800},
    "XML018266": {"nombre": "PLATANO", "precio": 900},
    "XML018267": {"nombre": "UVA", "precio": 1800},
    "XML018268": {"nombre": "PERA", "precio": 1100},
    "XML018269": {"nombre": "PIÑA", "precio": 2200},
    "XML018270": {"nombre": "MANGO", "precio": 1500},
    "XML018271": {"nombre": "FRESA", "precio": 2000},
    "XML018272": {"nombre": "PAPAYA", "precio": 1700},
    "XML018273": {"nombre": "KIWI", "precio": 1600},
    "XML018274": {"nombre": "DURAZNO", "precio": 1300},
    "XML018275": {"nombre": "CEREZA", "precio": 2800},
    "XML018276": {"nombre": "LIMON", "precio": 700},
    "XML018277": {"nombre": "MANDARINA", "precio": 850},
    "XML018278": {"nombre": "GRANADA", "precio": 1900},
    "XML018279": {"nombre": "HIGO", "precio": 2100},
    "XML018280": {"nombre": "COCO", "precio": 2300},
    "XML018281": {"nombre": "MARACUYA", "precio": 2400},
    "XML018282": {"nombre": "GUAYABA", "precio": 1400},
    "XML018283": {"nombre": "LECHUGA", "precio": 950},
    "XML018284": {"nombre": "TOMATE", "precio": 1100},
    "XML018285": {"nombre": "ZANAHORIA", "precio": 750},
    "XML018286": {"nombre": "PEPINO", "precio": 850}
}

# Define la clase Producto para representar un artículo en la tienda
class Producto:
    # Método constructor que inicializa un producto con código, nombre y precio
    def __init__(self, codigo: str, nombre: str, precio:float):
        # Atributo: código único identificador del producto
        self.codigo = codigo
        # Atributo: nombre descriptivo del producto
        self.nombre = nombre 
        # Atributo: precio de venta del producto
        self.precio = precio
    
# Define la clase Inventario para gestionar el stock de productos
class Inventario:
    # Método constructor que inicializa el inventario
    def __init__(self):
        # Diccionario que almacena productos usando el código como clave
        self.productos: Dict[str, Producto] = {}
        
    # Método para verificar si un producto existe en el inventario
    def producto_existe(self, codigo: str) -> bool:
        # Retorna True si el código existe en el diccionario de productos
        return codigo in self.productos
    
    # Método para agregar un nuevo producto al inventario
    def agregar_producto(self, producto: Producto):
        # Verifica si el producto ya existe antes de agregarlo
        if self.producto_existe(producto.codigo):
            # Mensaje de error si el producto ya existe
            print(f"El producto con codigo {producto.codigo} ya existe.")
            return False  # Retorna False indicando que no se pudo agregar
        
        # Agrega el producto al diccionario usando el código como clave
        self.productos[producto.codigo] = producto
        # Mensaje de confirmación de agregado exitoso
        print(f"El producto con codigo {producto.codigo} ha sido agregado con exito.")
        return True  # Retorna True indicando éxito en la operación
            
    # Método para obtener información de todos los productos
    def mostrar_productos(self):
        # Retorna un diccionario con información resumida de todos los productos
        return {codigo: {"nombre": p.nombre, "precio": p.precio} for codigo, p in self.productos.items()}

# Define la clase CajaRegistradora para procesar ventas (actualmente básica)
class CajaRegistradora:
    # Método constructor que recibe una referencia al inventario
    def __init__(self, inventario: Inventario):
        # Almacena referencia al inventario para consultar productos
        self.inventario = inventario

# Define la clase Tienda que coordina el inventario y la caja registradora
class Tienda:
    # Método constructor que inicializa la tienda
    def __init__(self):
        # Crea una instancia de Inventario para gestionar productos
        self.inventario = Inventario()
        # Crea una instancia de CajaRegistradora pasando el inventario
        self.caja = CajaRegistradora(self.inventario)
        
    # Método para agregar productos a través de la tienda
    def agregar_producto(self, codigo: str, nombre: str, precio:float):
        # Crea una instancia de Producto con los parámetros recibidos
        producto = Producto(codigo,nombre,precio)
        # Delega la operación de agregado al inventario
        self.inventario.agregar_producto(producto)
        
    # Método para obtener información de todos los productos
    def mostrar_productos(self):
        # Delega la operación al método correspondiente del inventario
        return self.inventario.mostrar_productos()
    
tienda = Tienda()
tienda.agregar_producto("XML019286","JOJOTO",2500)
tienda.agregar_producto("XML018262", "MELON",2500)
tienda.agregar_producto("XML018263","SANDIA" ,1200 )
tienda.agregar_producto("XML018264", "MANZANA", 1200)
tienda.agregar_producto("XML018265", "PLATANO", 900)
tienda.agregar_producto("XML018267", "UVA", 1800)
tienda.agregar_producto("XML018268", "PERA", 1100)
tienda.agregar_producto("XML018269", "PIÑA", 2200)
tienda.agregar_producto("XML018270", "MANGO", 1500)
tienda.agregar_producto("XML018271", "FRESA", 2000)
tienda.agregar_producto("XML018272", "PAPAYA", 1700)
tienda.agregar_producto("XML018273", "KIWI", 1600)
tienda.agregar_producto("XML018274", "DURAZNO", 1300)
tienda.agregar_producto("XML018275", "CEREZA", 2800)
tienda.agregar_producto("XML018276", "LIMON", 700)
tienda.agregar_producto("XML018277", "MANDARINA", 850)
tienda.agregar_producto("XML018278", "GRANADA", 1900)
tienda.agregar_producto("XML018279", "HIGO", 2100)
tienda.agregar_producto("XML018280", "COCO", 2300)
tienda.agregar_producto("XML018281", "MARACUYA", 2400)
tienda.agregar_producto("XML018282", "GUAYABA", 1400)
tienda.agregar_producto("XML018283", "LECHUGA", 950)
tienda.agregar_producto("XML018284", "TOMATE", 1100)
tienda.agregar_producto("XML018285", "ZANAHORIA", 750)
tienda.agregar_producto("XML018286", "PEPINO", 850)

print(tienda.mostrar_productos())