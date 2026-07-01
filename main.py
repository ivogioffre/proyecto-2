from pokedex_medallas import pokedex_nacional, registro_medallas
from captura import capturar_pokemon
from pc_centro import PC, curar_equipo
import os 
from time import sleep 
from oak_gimnasio import StackTransferencias,transferir_pokemon,deshacer_transferencia,desafiar_gimnasio
from ordenamiento import ordenar_pc
from busqueda import buscar_pokemon_equipo, buscar_pokemon_pokedex

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
        print("5. Ordenar PC ")
        print("6. Enviar Pokémon al Centro Pokémon")
        print("7. Transferir Pokémon al Profesor Oak ")
        print("8. Deshacer última transferencia ")
        print("9. Desafiar Líder de Gimnasio")
        print("10. Ver Medallas")
        print("11. Salir del sistema")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            os.system("cls")
            buscar_pokemon_pokedex(pokedex)

        elif opcion == "2":
            os.system("cls")
            buscar_pokemon_equipo(equipo)

        elif opcion == "3":
            os.system("cls")
            pc.mostrar_pc()

        elif opcion == "4":
            os.system("cls")
            capturar_pokemon(pokedex, equipo, pc)

        elif opcion == "5":
             os.system("cls")
             ordenar_pc(pc)

        elif opcion == "6":
            os.system("cls")
            curar_equipo(equipo)

        elif opcion == "7":
            os.system("cls")
            transferir_pokemon(pc, transferencias)

        elif opcion == "8":
            os.system("cls")
            deshacer_transferencia(pc, transferencias)

        elif opcion == "9":
            os.system("cls")
            desafiar_gimnasio(equipo,medallas)
        elif opcion == "10":
            os.system("cls")
            ver_medallas(medallas)
        elif opcion == "11":
            os.system("cls")
            print("Saliendo del sistema...")
            sleep(1)
            os.system("cls")
            break

        else:
            os.system("cls")
            print("Opcion inválida")
            sleep(1)
            os.system("cls")


if __name__ == "__main__":
    main()