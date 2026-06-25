from time import sleep

def equipo_activo (pokemon, equipo, pc): #creamos el equipo activo con una lista de maximo 6 pokemones 
    if len(equipo) < 6:
        equipo.append(pokemon)
        print(f" {pokemon.nombre} agregado al equipo principal  (b^ー°)")
    else:
        
        pc.agregar_pokemon(pokemon)
        print(f"El equipo principal ya esta completo por lo que el pokemon:{pokemon.nombre} ha sido enviado a la PC  (b^ー°)")



class Nodo:
    def __init__(self, pokemon):
        self.pokemon = pokemon  #creamos la dinamica del nodo con el pokemon almacenado y la direccion del siguiente nodo 
        self.next = None        #de esta manera podemos simular una linked list 


class PC:#creamos el almacenamiento ilimitado de pokemones utilizando una linked list 
    def __init__(self):
        self.head = None #variable head apunta al primer nodo de la  lista 

    def agregar_pokemon(self, pokemon):
        nuevo = Nodo(pokemon)

        if self.head is None:
            self.head = nuevo # se establece al primer pokemon como head de la lista 
            return

        actual = self.head

        while actual.next:
            actual = actual.next

        actual.next = nuevo

    def esta_vacia(self):
        return self.head is None

    def tamaño(self):
        contador = 0
        actual = self.head

        while actual:
            contador += 1
            actual = actual.next

        return contador

    def mostrar_pc(self):  # se muestran los pokemones de la pc 
        if self.esta_vacia():
            print("La PC esta vacia ¯\_(ツ)_/¯ ")
            return

        actual = self.head

        print("---- PC POKEMON ----")

        while actual:
            print(actual.pokemon)
            actual = actual.next

class CentroPokemon:  # establecemos el cento pokemon como una queue
    def __init__(self):
        self.queue = []

    def ingresar(self, pokemon):
        self.queue.append(pokemon)

    def curar_siguiente(self):
        if self.is_empty():
            return None

        return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def mostrar_equipo(equipo):

    if len(equipo) == 0:
        print("No hay pokemones en el equipo :(")
        return

    print("---- EQUIPO ACTIVO ----") # se muestra el equipo activo 
    for pokemon in equipo:
        print(pokemon)


def curar_equipo(equipo):
    if len(equipo) == 0:
        print("No hay pokemones para curar :)")
        return
    centro = CentroPokemon()
    for pokemon in equipo:
        centro.ingresar(pokemon)

    print("Curando equipo (︶｡︶)zzz ")
    sleep(2)
    while not centro.is_empty():
        pokemon = centro.curar_siguiente() # simulamos la sancion usando la queue
        print(f"{pokemon}  ---> fue curado")    # el primer pokemon que entra al  centro es el primero que se va 
        sleep(0.5)
    print("Pokemones curados con exito")

if __name__ == "__main__":

    equipo = []

    pc = PC()
