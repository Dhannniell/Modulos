
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

class Producto:
    def __init__(self, codigo: str, nombre: str, precio:float):
        self.codigo = codigo
        self.nombre = nombre 
        self.precio = precio
    
class Inventario:
    def __init__(self):
        self.productos: Dict[str, Producto] = {}
        
        
    def producto_existe(self, codigo: str) -> bool:
        return codigo in self.productos
    
    
    def agregar_producto(self, producto: Producto):
        if self.producto_existe(producto.codigo):
            print(f"El producto con codigo {producto.codigo} ya existe.")
            return False
        
        self.productos[producto.codigo] = producto
        print(f"El producto con codigo {producto.codigo} ha sido agregado con exito.")
        return True
            
    def mostrar_productos(self):
        return {codigo: {"nombre": p.nombre, "precio": p.precio} for codigo, p in self.productos.items()}

class CajaRegistradora:
    def __init__(self, inventario: Inventario):
        self.inventario = inventario
        self.ventas: Dict[str, float] = {}

    def realizar_compra(self, codigo_producto: str, cantidad: int):
        
        if codigo_producto not in self.inventario.productos:
            print("El producto no existe")
            return
        
        producto = self.inventario.productos[codigo_producto]
        total = producto.precio * cantidad
        self.ventas[codigo_producto] = self.ventas.get(codigo_producto,0) + total
        print(f"Compra realizada: {cantidad} x {producto.nombre} = ${total}")
    
    
class Tienda:
    def __init__(self):
        self.inventario = Inventario()
        self.caja = CajaRegistradora(self.inventario)
        
    def agregar_producto(self, codigo: str, nombre: str, precio:float):
        producto = Producto(codigo,nombre,precio)
        self.inventario.agregar_producto(producto)
        
    def mostrar_productos(self):
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

tienda.caja.realizar_compra("XML018286",5)