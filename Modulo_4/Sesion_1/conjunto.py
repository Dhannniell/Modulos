# Conjunto (set) en Python
# App de gestion de clientes (unicos) de una campaña de mercadeo

from typing import Set

def obtener_clientes_unicos(clientes: Set[str], nuevos_clientes: Set[str]) -> Set[str]:
    return clientes.union(nuevos_clientes)

def gestionar_clientes(clientes: Set[str]) -> None:
    
    #Agregar un cliente
    clientes.add("Pedro")
    print("Cliented despues de agregar a Pedro", clientes)
    
    #Agregar un cliente duplicado
    clientes.add("Carlos")
    print("Cliented despues de agregar intentar agregar a Carlos", clientes)
    
    # Uso de la funcion "remove" para eliminar un cliente (si existe el cliente, y si no -> ERROR)
    cliente = "Ana"
    clientes.remove(cliente)
    print("Clientes despues de eliminar a Ana con el metodo remove", clientes)
    
    # Uso de la funcion discard para eliminar un elemento del Set 
    cliente2 = "Luis"
    clientes.discard(cliente2)
    print("Clientes despues de eliminar a Luis con el metodo Discard: ", clientes)
    
    # Uso del metodo POP para mostrar un elemento y posterior lo borra automaticamente 
    cliente_removido = clientes.pop()
    print(f"Cliente removido aleatoriamente: {cliente_removido}")
    print("Clientes restantes:", clientes)
    
    # Borrar todos los elementos del Set 
    clientes.clear()
    print("Clientes despues del metodo Clear: ", clientes)
    
def main():
    
    clientes_antiguos = {"Carlos", "Ana", "Luis"}
    clientes_nuevos = {"Luis", "Maria", "Jorge"}
    clientes_finales = obtener_clientes_unicos(clientes_antiguos, clientes_nuevos)
    print("La lista actualizada de clientes es : ", clientes_finales)
    
    gestionar_clientes(clientes_finales)

if __name__ == "__main__":
    main()