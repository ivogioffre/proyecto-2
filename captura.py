import random
from pc_centro import equipo_activo


def capturar_pokemon(pokedex, equipo, pc):

    pokemones = pokedex.obtener_valores() # se buscan los pokemones de la pokedex

    if not pokemones:
        print("La Pokedex está vacia")
        return

    pokemon = random.choice(pokemones) # se elije un pokemon random de la pokedex
    print("\n")
    print(f"--- SISTEMA DE CAPTURA ---")
    print(f"Ha aparecido un {pokemon.nombre} salvaje (PC: {pokemon.pc})")

    respuesta = input("¿Intentar capturarlo? (s/n): ").strip().lower()
    if respuesta != "s":
        print(f"{pokemon.nombre} escapo  (╥﹏╥)")
        return

    equipo_activo(pokemon, equipo, pc) # si la respuestaa es "s" el pokemon se guarda en el equipo o pc segun la funcion -equipo_activo-