from time import sleep 
import os 

def busqueda_lineal(equipo, nombre):  # busqueda binaria en el equipo principal utilizando los algoritmos trabajados en clase previamente 
    for pokemon in equipo:
        if pokemon.nombre.lower() == nombre.lower():
            return pokemon

    return None


def buscar_pokemon_equipo(equipo):  # submenu del equipo 
    if len(equipo) == 0:
        print("No hay pokemones en el equipo")
        sleep(1)
        return

    while True:
        print("------ EQUIPO PRINCIPAL ------")
        print("1. Ver equipo")
        print("2. Buscar Pokemon por nombre")
        print("3. Volver")

        opcion = input("Seleccione una opcion: ")
        os.system("cls")
        if opcion == "1":
            print("\n---- EQUIPO ACTIVO ----")
            for pokemon in equipo:
                print(pokemon)
            seguir = input("Inserte cualquier boton para continuar : ")
            os.system("cls")
            return

        elif opcion == "2":
            nombre = input("Ingrese el nombre del Pokemon: ")
            pokemon = busqueda_lineal(equipo, nombre)
            if pokemon:
                print("Pokemon encontrado:")
                print(pokemon)
            else:
                print("El pokemon solicitado no se encuentra en el equipo")
            sleep(1)

            return
        elif opcion == "3":
            return
        else:
            print("ERROR")


def busqueda_binaria(lista, objetivo): # busqueda binaria en la pokedex utilizando los algoritmos trabajados en clase previamente 
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio

        elif lista[medio] < objetivo:
            izquierda = medio + 1

        else:
            derecha = medio - 1

    return -1


def buscar_pokemon_pokedex(pokedex): # submenu buscar en pokedex 

    while True:

        print("------ POKEDEX ------")
        print("1. Ver Pokedex completa")
        print("2. Buscar Pokemon por ID")
        print("3. Volver")

        opcion = input("Seleccione una opcion: ")
        os.system("cls")
        if opcion == "1":
            print("\n")
            print("---- POKEDEX NACIONAL ----")
            for pokemon in pokedex.obtener_valores():
                print(pokemon)
            seguir = input("Inserte cualquier boton para continuar : ")
            os.system("cls")
            return

        elif opcion == "2":
            try:
                id_pokemon = int(input("Ingrese el ID del Pokemon: ")) #usuario ingresa numero de id a buscar
            except:
                print("Debe ingresar un numero valido")
                continue
            ids = []
            for pokemon in pokedex.obtener_valores(): # convertimos pokedex en lista 
                ids.append(pokemon.id)
            ids.sort()

            indice = busqueda_binaria(ids, id_pokemon)

            if indice == -1:
                print("No existe un Pokemon con ese ID")
            else:
                print("\n")
                print("Pokemon encontrado:")
                print(pokedex.buscar(id_pokemon))
            sleep(1)
            return
        elif opcion == "3":
            return
        else:
            print("Opcion inválida")