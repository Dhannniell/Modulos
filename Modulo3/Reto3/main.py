import tkinter as tk
from tkinter import messagebox


#Modelo 
class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def reducir_stock(self, cantidad):
        if cantidad < self.stock:
            self.stock -= cantidad
            return True
        return False

class Modelo:
    def __init__(self):
        self.productos = {
            1:Producto(1, "Manzana", 1000, 20),
            2:Producto(2, "Banana", 800, 30),
            3:Producto(3, "Pera", 1200, 15),
            4:Producto(4, "Uva", 2500, 12),
            5:Producto(5, "Fresa", 3000, 8),
            6:Producto(6, "Sandía", 5000, 5),
            7:Producto(7, "Melón", 4500, 7),
            8:Producto(8, "Piña", 3500, 10),
            9:Producto(9, "Mango", 2800, 9),
            10:Producto(10, "Papaya", 2200, 6),
            11:Producto(11, "Zanahoria", 900, 25),
            12:Producto(12, "Tomate", 1500, 18),
            13:Producto(13, "Papa", 700, 40),
            14:Producto(14, "Cebolla", 600, 35),
            15:Producto(15, "Espinaca", 1800, 12),
            16:Producto(16, "Brócoli", 2000, 10),
            17:Producto(17, "Lechuga", 1300, 20),
            18:Producto(18, "Pimiento", 1700, 15),
            19:Producto(19, "Pepino", 1100, 22),
            20:Producto(20, "Aguacate", 4000, 8)
        }
        self.historial_ventas = []
        
        
    def obtener_productos(self):
        return [f"{prod.id_producto} - {prod.nombre} - ${prod.precio} - Stock {prod.stock}" for prod in self.productos.values()]
    
    def obtener_historial(self):
        return self.historial_ventas
    
    def vender_producto(self, id_producto, cantidad):
        if id_producto in self.productos and self.productos[id_producto].reducir_stock(cantidad):
            total = self.productos[id_producto].precio * cantidad
            self.historial_ventas.append((self.productos[id_producto].nombre,cantidad,total))
            return total
        return None
    
#Controlador 
class Controlador:
    def __init__(self):
        self.modelo = Modelo()
    
    def obtener_productos(self):
        return self.modelo.obtener_productos()
    
    def agregar_al_carrito(self, producto_str, cantidad, carrito):
        id_producto = int(producto_str.split(" - ")[0])
        total = self.modelo.vender_producto(id_producto, cantidad)
        if total is not None:
            if id_producto in carrito:
                carrito[id_producto]["cantidad"] += cantidad
                carrito[id_producto] ["total"] += total
            else:
                carrito[id_producto] = {"nombre": self.modelo.productos[id_producto].nombre, "cantidad":cantidad, "total":total}
        else:
            messagebox.showerror("Error", "Stock insuficiente")
            
    def finalizar_compra(self, carrito, total_var):
        if not carrito:
            messagebox.showerror("Error", "El carrito esta vacio")
            return
        mensaje = "Compra Finalizada"
        for id_producto, total in carrito.items():
            mensaje += f"{self.modelo.productos[id_producto].nombre}: ${total}"
        messagebox.showinfo("Compra Realizada", mensaje)
        carrito.clear()
        total_var.set("Total: $0")
    
    def ver_historial(self):
        pass
        
    
#Vista
class Vista():
    def __init__(self, root, controlador):
        self.controlador = controlador
        self.root = root 
        self.root.title("Caja Registradora - Fruver")
        
        self.carrito = {}
        self.total = tk.StringVar(value="Total: $0")
        self.cantidad_var = tk.StringVar()
        
        frame = tk.Frame(root)
        frame.pack()
        
        self.lista_productos = tk.Listbox(frame)
        
        for prod in self.controlador.obtener_productos():
            self.lista_productos.insert(tk.END, prod)
        self.lista_productos.grid(row=0, column=0)
        
        self.lista_carrito = tk.Listbox(frame)
        self.lista_carrito.grid(row=0, column=1)
        
        tk.Entry(root, textvariable=self.cantidad_var).pack()
        
        tk.Button(root, text="Agregar", command=self.agregar_producto).pack()
        tk.Button(root, text="Cancelar").pack()
        tk.Button(root, text="Finalizar Compra").pack()
        tk.Button(root, text="Ver Historial").pack()
        
        tk.Label(root, textvariable=self.total).pack()
        
    def actualizar_total(self):
        self.total.set(f"Total: ${sum(item['total'] for item in self.carrito.values())}")
        self.actualizar_carrito()
        
    def actualizar_carrito(self):
        self.lista_carrito.delete(0, tk.END)
        for item in self.carrito.values():
            self.lista_carrito.insert(tk.END, f"{item['nombre']} - {item["cantidad"]} - ${item['total']}")
            
        
    def agregar_producto(self):
        producto = self.lista_productos.get(tk.ACTIVE)
        cantidad = self.cantidad_var.get()
            
        if cantidad.isdigit():
            cantidad = int(cantidad)
            self.controlador.agregar_al_carrito(producto,cantidad,self.carrito)
            self.actualizar_total()
        else:
            messagebox.showerror("Error", "Ingrese una cantidad valida")




#Main

root = tk.Tk()
controlador = Controlador()
app = Vista(root, controlador)
root.mainloop()