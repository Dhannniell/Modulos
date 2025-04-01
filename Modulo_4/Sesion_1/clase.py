# Listas en Python

productos = ["Carne", "Papa", "Tomate"]
productos.append("Yuca")
print(productos)

# Tuplas en Python 
Codigo_Postal = (45400, "Zipaquira")
print(Codigo_Postal)
#Codigo_Postal[0] = 45400
# print(Codigo_Postal)

# Set (conjuntos) en Python

categorias = {"Terror", "Drama", "Sci-Fi"}
categorias.add("Suspenso")
print(categorias)

# Diccionarios (dict) en Python

clientes = {
    "ID": 1010,
    "Nombre": "Luis",
    "Apellido": "Molero"
    
}
clientes["Email"] = "luis@gmail.com"
clientes["Direccion"] = "Cra 78 125A-43"
print(clientes)