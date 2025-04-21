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
    
    # Uso de la funcion "remove" para eliminar un cliente (si existe el cliente), y si no -> ERROR
    clientes = "Ana"
    clientes.remove("Ana")
    print("Cliented despues de eliminar a Ana", clientes)