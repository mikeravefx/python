# 1a) Programa para almacenar los regalos pedidos por los niños
def gestionar_regalos() -> list:
    regalos = []  # Lista para almacenar los regalos
    print("Bienvenido al programa de gestión de regalos")
    
    while True:
        regalo = input("Escribe un regalo: ")  # Pedir el regalo
        regalos.append(regalo)  # Añadir el regalo a la lista
        
        # Preguntar si el usuario quiere seguir añadiendo regalos
        continuar = input("¿Quieres introducir más regalos? Escribe No para terminar: ").lower()
        if continuar == "no":
            break  # Salir del bucle si la respuesta es "No"
    
    return regalos

# Ejemplo de uso
regalos = gestionar_regalos()
print(regalos)


# 1b) Función para contar cuántas veces se ha pedido un regalo
def contar_regalos(regalos: list, regalo_buscado: str) -> int:
    """
    Esta función recibe una lista de regalos y un regalo que se busca,
    y devuelve cuántas veces aparece en la lista.
    """
    return regalos.count(regalo_buscado)

# Ejemplo de uso
regalo_buscado = "monopoly"
cantidad = contar_regalos(regalos, regalo_buscado)
print(f"El regalo '{regalo_buscado}' ha sido pedido {cantidad} veces.")
