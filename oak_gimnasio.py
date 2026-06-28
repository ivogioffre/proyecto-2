import random
from time import sleep 

class StackTransferencias: # stak de transferencias al profesor Oak
    def __init__(self):
        self.stack = []

    def push(self, pokemon):
        if len(self.stack) == 5: #maximo 5 pokemones
            eliminado = self.stack.pop(0)
            print(f"se elimino del historial la transferencia de {eliminado.nombre} (︶︹︶)")

        self.stack.append(pokemon)

    def pop(self):
        if len(self.stack) == 0:
            return None

        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None

        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


def transferir_pokemon(pc, transferencias): # funcion que se encarga de las transferencias 
    if pc.esta_vacia(): 
        print("La PC esta vacia")
        sleep(1)
        return
    pc.mostrar_pc_numerada()

    try:
        posicion = int(input("seleccione el pokemon a transferir por numero: "))
    except:
        print("opcion invalida")
        sleep(1)
        return

    pokemon = pc.eliminar_por_posicion(posicion) # se elimina el pokemon deseado de la pc 

    if pokemon is None:
        print("No existe ese pokemon")
        sleep(1)
        return

    transferencias.push(pokemon)

    print(f"{pokemon.nombre} fue transferido al Profesor Oak")
    sleep(1)


def deshacer_transferencia(pc, transferencias):

    if transferencias.is_empty():
        print("no hay transferencias para deshacer")
        sleep(1)
        return

    pokemon = transferencias.pop() # se elimina de el stack

    pc.agregar_pokemon(pokemon) # se agrega nuevamente a la pc 

    print(f"{pokemon.nombre} regreso a la PC  (*^▽^*)")
    sleep(1)


def desafiar_gimnasio(equipo,medallas):

    if len(equipo) == 0:
        print("no tenes pokemones en tu equipo para desafiar un gimnasio")
        return

    gimnasios = [   # usamos los mismos gimnasios que las medallas
        "Medalla Roca",
        "Medalla Cascada",
        "Medalla Trueno",
        "Medalla Arcoiris",
        "Medalla Alma",
        "Medalla Pantano",
        "Medalla Volcan",
        "Medalla Tierra"
    ]

    print("------ GIMNASIOS ------")

    for i in range(len(gimnasios)):
        print(f"{i + 1}. {gimnasios[i]}") # enumeramos gimnasio 

    try:
        opcion = int(input("seleccione un gimnasio: "))
    except:
        print("opcion invalida")
        sleep(1)
        return

    if opcion < 1 or opcion > len(gimnasios):
        print("Opcion invalida")
        sleep(1)
        return

    medalla = gimnasios[opcion - 1]

    print("Comenzando batalla...")
    sleep(1)

    gano = random.choice([True, False])

    if gano:

        if medallas.buscar(medalla):
            print(f"Ganaste el combate pero ya tenias la {medalla}")
        else:
            medallas.agregar(medalla)
            print(f"Felicidades obtuviste la {medalla}")

    else:
        print("Perdiste el combate GG")
        sleep(1)