from time import sleep

def bubble_sort_nombre(lista): # bubble sort segun el nombre de pokemon (obtenido de los ejercicios hechos en clase)
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j].nombre > lista[j + 1].nombre:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


def selection_sort_tipo(lista): #selection sort segun el tipo  (obtenido de los ejercicios hechos en clase)
    n = len(lista)

    for i in range(n):
        minimo = i

        for j in range(i + 1, n):
            if lista[j].tipo < lista[minimo].tipo:
                minimo = j

        lista[i], lista[minimo] = lista[minimo], lista[i]

    return lista


def quick_sort_pc(lista, minimo, maximo): #quick sort segun el pc del pokemon (obtenido de los ejercicios hechos en clase)

    if minimo < maximo: # caso base que pone fin a la recursividad

        pivote = particion(lista, minimo, maximo)

        quick_sort_pc(lista, minimo, pivote - 1) #aplicamos recursividad en las subdivisiones hasta ordenar la lista
        quick_sort_pc(lista, pivote + 1, maximo)

    return lista


def particion(lista, minimo, maximo):

    pivote = lista[maximo]
    i = minimo - 1

    for j in range(minimo, maximo):

        if lista[j].pc >= pivote.pc:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[maximo] = lista[maximo], lista[i + 1]

    return i + 1


def ordenar_pc(pc):

    if pc.esta_vacia():
        print("La PC esta vacia (•ิ_•ิ)")
        return
    while True: #creamos submenu en bucle 
        print("\n")
        print("------ ORDENAR PC ------")
        print("1. Ordenar alfabeticamente")
        print("2. Ordenar por tipo")
        print("3. Ordenar por poder de combate")
        print("4. Volver")

        print("¿Como deseas ordenar la PC?")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            pokemones = pc.obtener_pokemones()

            bubble_sort_nombre(pokemones)

        elif opcion == "2":

            pokemones = pc.obtener_pokemones()

            selection_sort_tipo(pokemones)

        elif opcion == "3":
            pokemones = pc.obtener_pokemones()

            quick_sort_pc(pokemones, 0, len(pokemones) - 1)
        elif opcion == "4":
            return
        else:
            print("opcion invalida")
            continue

        pc.vaciar() # vaciamos la linked list 

        for pokemon in pokemones: #agregamos los pokemones con la lista ya ordenada 
            pc.agregar_pokemon(pokemon)

        print("la PC fue ordenada correctamente")
        sleep(1)
        return