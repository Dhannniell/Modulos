# App: Gestion de pedidos de una tienda

def agregar_pedido(pedidos: list[str], nuevo_pedido:str) -> list[str]:
    pedidos.append(nuevo_pedido)
    return pedidos

def eliminar_pedido(pedidos: list[str], pedido_a_eliminar: str) -> list[str]:
    if pedido_a_eliminar in pedidos:
        pedidos.remove(pedido_a_eliminar)
    else:
        print("El pedido no se encuentra en la lista.")
    return pedidos

def buscar_pedido(pedidos: list[str], pedido_a_buscar: str) -> int:
    if pedido_a_buscar in pedidos:
        return pedidos.index(pedido_a_buscar)
    else:
        print("El pedido no se encuentra en la lista.")
        return -1

def main():
    