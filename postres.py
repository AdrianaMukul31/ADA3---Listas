class NodoIngrediente:
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente
        self.siguiente = None

class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None
        self.siguiente = None

class ListaPostres:
    def __init__(self):
        self.cabeza = None

   
    def agregar_postre(self, nombre):
        nuevo_postre = NodoPostre(nombre)
        if not self.cabeza:
            self.cabeza = nuevo_postre
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_postre
        print(f"Postre '{nombre}' agregado.")

    def eliminar_postre(self, nombre_postre):
        nodo_actual = self.cabeza
        nodo_anterior = None
        while nodo_actual:
            if nodo_actual.nombre == nombre_postre:
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                else:
                    self.cabeza = nodo_actual.siguiente
                self._eliminar_ingredientes(nodo_actual)
                print(f"Postre '{nombre_postre}' y todos sus ingredientes eliminados.")
                return
            nodo_anterior, nodo_actual = nodo_actual, nodo_actual.siguiente
        print(f"Postre '{nombre_postre}' no encontrado.")

    def _eliminar_ingredientes(self, nodo_postre):
        nodo_ingrediente_actual = nodo_postre.ingredientes
        while nodo_ingrediente_actual:
            siguiente_ingrediente = nodo_ingrediente_actual.siguiente
            del nodo_ingrediente_actual
            nodo_ingrediente_actual = siguiente_ingrediente

    def agregar_ingrediente(self, nombre_postre, ingrediente):
        nodo_postre = self.buscar_postre(nombre_postre)
        if nodo_postre:
            nuevo_ingrediente = NodoIngrediente(ingrediente)
            if not nodo_postre.ingredientes:
                nodo_postre.ingredientes = nuevo_ingrediente
            else:
                nodo_actual = nodo_postre.ingredientes
                while nodo_actual.siguiente:
                    nodo_actual = nodo_actual.siguiente
                nodo_actual.siguiente = nuevo_ingrediente
            print(f"Ingrediente '{ingrediente}' agregado al postre '{nombre_postre}'.")
        else:
            print(f"Postre '{nombre_postre}' no encontrado.")

    def eliminar_ingrediente(self, nombre_postre, ingrediente):
        nodo_postre = self.buscar_postre(nombre_postre)
        if nodo_postre:
            nodo_actual = nodo_postre.ingredientes
            nodo_anterior = None
            while nodo_actual:
                if nodo_actual.ingrediente == ingrediente:
                    if nodo_anterior:
                        nodo_anterior.siguiente = nodo_actual.siguiente
                    else:
                        nodo_postre.ingredientes = nodo_actual.siguiente
                    print(f"Ingrediente '{ingrediente}' eliminado de '{nombre_postre}'.")
                    return
                nodo_anterior, nodo_actual = nodo_actual, nodo_actual.siguiente
            print(f"Ingrediente '{ingrediente}' no encontrado en '{nombre_postre}'.")
        else:
            print(f"Postre '{nombre_postre}' no encontrado.")

    def buscar_postre(self, nombre_postre):
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.nombre == nombre_postre:
                return nodo_actual
            nodo_actual = nodo_actual.siguiente
        return None

    def imprimir_ingredientes(self, nombre_postre):
        nodo_postre = self.buscar_postre(nombre_postre)
        if nodo_postre:
            nodo_actual = nodo_postre.ingredientes
            if not nodo_actual:
                print(f"No hay ingredientes en '{nombre_postre}'.")
            else:
                print(f"Ingredientes de '{nombre_postre}':")
                while nodo_actual:
                    print(f"- {nodo_actual.ingrediente}")
                    nodo_actual = nodo_actual.siguiente
        else:
            print(f"Postre '{nombre_postre}' no encontrado.")

    def imprimir_todos_postres(self):
        nodo_actual = self.cabeza
        if not nodo_actual:
            print("No hay postres en la lista.")
            return
        print("Lista de postres y sus ingredientes:")
        while nodo_actual:
            print(f"Postre: {nodo_actual.nombre}")
            self.imprimir_ingredientes(nodo_actual.nombre)
            nodo_actual = nodo_actual.siguiente
            print()  

  #PROGRAMA 2
    def eliminar_postres_repetidos(self):
        if not self.cabeza:
            return

        nombres_vistos = set()
        nodo_actual = self.cabeza
        nodo_anterior = None

        while nodo_actual:
            if nodo_actual.nombre in nombres_vistos:
                
                nodo_anterior.siguiente = nodo_actual.siguiente
                self._eliminar_ingredientes(nodo_actual)  
                print(f"Postre '{nodo_actual.nombre}' eliminado por ser duplicado.")
            else:
                nombres_vistos.add(nodo_actual.nombre)
                nodo_anterior = nodo_actual

            nodo_actual = nodo_anterior.siguiente if nodo_anterior else self.cabeza


def menu():
    lista_postres = ListaPostres()
    opciones = {
        "1": lambda: lista_postres.agregar_postre(input("Ingresa el nombre del postre: ")),
        "2": lambda: lista_postres.eliminar_postre(input("Ingresa el nombre del postre a eliminar: ")),
        "3": lambda: lista_postres.agregar_ingrediente(input("Ingresa el nombre del postre: "), input("Ingresa el ingrediente a agregar: ")),
        "4": lambda: lista_postres.eliminar_ingrediente(input("Ingresa el nombre del postre: "), input("Ingresa el ingrediente a eliminar: ")),
        "5": lambda: lista_postres.imprimir_ingredientes(input("Ingresa el nombre del postre: ")),
        "6": lista_postres.imprimir_todos_postres,
        "7": lista_postres.eliminar_postres_repetidos,
        "8": exit
    }

    while True:
        print("\n--- Menú ---")
        print("1. Agregar postre")
        print("2. Eliminar postre")
        print("3. Agregar ingrediente a un postre")
        print("4. Eliminar ingrediente de un postre")
        print("5. Imprimir ingredientes de un postre")
        print("6. Imprimir todos los postres")
        print("7. Eliminar postres repetidos")
        print("8. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción no válida. Intenta de nuevo.")


menu()