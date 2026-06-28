from pokedex_medallas import pokedex_nacional, registro_medallas
from captura import capturar_pokemon
from pc_centro import PC, mostrar_equipo, curar_equipo
import os 
from time import sleep 
from oak_gimnasio import StackTransferencias,transferir_pokemon,deshacer_transferencia,desafiar_gimnasio

def ver_pokedex(pokedex):   # creamos funcion ver_pokedex del metodo obtener_valores de la pokedex 
    pokemones = pokedex.obtener_valores()

    if len(pokemones) == 0:
        print("La Pokedex está vacia")
        return
    print("\n")
    print("---- POKEDEX NACIONAL ----")
    for pokemon in pokemones:
        print(pokemon)
    seguir = input("Inserte cualquier boton para continuar : ")
    os.system("cls")
    return

def ver_medallas(medallas): # creamos funcion que nos permitira ver las medallas que obtuvimos(2 de default)

    lista = medallas.obtener_medallas()
    if len(lista) == 0:
        print("No tenes medallas.")
        return
    print("---- MEDALLAS OBTENIDAS ----")
    for medalla in lista:
        print(medalla)
    seguir = input("Inserte cualquier boton para continuar : ")
    os.system("cls")
    return


def main():
    os.system("cls")
    print("   SISTEMA DE GESTIÓN: POKÉMON HUERGO   ")
    sleep(0.5)
    print("Inicializando motor de base de datos... OK.")
    sleep(0.5)
    print("Cargando Pokédex Nacional... OK.")
    sleep(0.5)
    print("Validando registros de medallas... OK.")
    sleep(0.5)
    os.system("cls")


    pokedex = pokedex_nacional()
    medallas = registro_medallas()

    equipo = [] # array equipo principal 
    pc = PC()   # linked list pc
    transferencias = StackTransferencias() #transferencias al profesor Oak

    while True: # repetimos el menu principal en bucle
        print("\n--- MENU PRINCIPAL ---")
        print("1. Ver Pokédex")
        print("2. Ver Equipo Principal")
        print("3. Ver PC")
        print("4. Capturar nuevo Pokémon")
        print("5. Ordenar PC (pendiente)")
        print("6. Buscar Pokémon en Equipo (pendiente)")
        print("7. Enviar Pokémon al Centro Pokémon")
        print("8. Transferir Pokémon al Profesor Oak ")
        print("9. Deshacer última transferencia ")
        print("10. Desafiar Líder de Gimnasio")
        print("11. Ver Medallas")
        print("12. Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system("cls")
            ver_pokedex(pokedex)

        elif opcion == "2":
            os.system("cls")
            mostrar_equipo(equipo)

        elif opcion == "3":
            os.system("cls")
            pc.mostrar_pc()

        elif opcion == "4":
            os.system("cls")
            capturar_pokemon(pokedex, equipo, pc)

        elif opcion == "5":
            print("no implementado")

        elif opcion == "6":
            print("no implementado")

        elif opcion == "7":
            os.system("cls")
            curar_equipo(equipo)

        elif opcion == "8":
            os.system("cls")
            transferir_pokemon(pc, transferencias)

        elif opcion == "9":
            os.system("cls")
            deshacer_transferencia(pc, transferencias)

        elif opcion == "10":
            os.system("cls")
            desafiar_gimnasio(equipo,medallas)
        elif opcion == "11":
            os.system("cls")
            ver_medallas(medallas)
        elif opcion == "12":
            os.system("cls")
            print("Saliendo del sistema...")
            sleep(1)
            os.system("cls")
            break

        else:
            os.system("cls")
            print("Opcion invalida")
            sleep(1)
            os.system("cls")


if __name__ == "__main__":
    main()