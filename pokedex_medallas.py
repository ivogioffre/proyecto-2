import json
from pokemon import Pokemon

class HashMap:

    def __init__(self, size=50):
        self.size = size
        self.buckets = [[] for poke in range(size)]  # creamos las buckets usando el tamaño total de los pokemones

    def funcion_hash(self, key):
        return hash(key) % self.size

    def agregar(self, key, value):  # se agregan los pokemones usando como key el id del pokemon y como value la instancia del mismo 
        indice = self.funcion_hash(key)

        for par in self.buckets[indice]:
            if par[0] == key:
                return

        self.buckets[indice].append([key, value]) #se agrega en el bucket indicado el pokemon 

    def buscar(self, key):
        indice = self.funcion_hash(key)

        for par in self.buckets[indice]:
            if par[0] == key:
                return par[1]

        return None

    def obtener_valores(self):
        valores = []

        for bucket in self.buckets:
            for par in bucket:
                valores.append(par[1])

        return valores

def pokedex_nacional():
    pokedex = HashMap()
    with open("pokemones.json","r",encoding="utf-8") as pokemon_json:
        lista_pokemon = json.load(pokemon_json)
    
    for poke in lista_pokemon:
        
        pokemon = Pokemon(poke["id"],poke["nombre"],poke["tipo"],poke["pc"])

        pokedex.agregar(pokemon.id, pokemon)

    return pokedex 

class HashSet:
    def __init__(self, size=8):
        self.size = size
        self.buckets = [[] for medalla in range(size)]

    def funcion_hash(self, key):
        return hash(key) % self.size  # se calcula el numero correspondiente a la medalla usando ademas la funcion hash()

    def agregar(self, key):         
        indice = self.funcion_hash(key)   # se agrega la medalla al bucket correspondiente 
        if key not in self.buckets[indice]:
            self.buckets[indice].append(key)

    def buscar(self, key):
        indice = self.funcion_hash(key)

        return key in self.buckets[indice]

    def obtener_medallas(self):
        medallas = []

        for bucket in self.buckets:
            for medalla in bucket:
                medallas.append(medalla)

        return medallas 


def registro_medallas():
    
    medallas = HashSet()
    
    with open("medallas.json", "r", encoding="utf-8") as medallas_json:
        lista_medallas = json.load(medallas_json)
    medallas.agregar(lista_medallas[0])  #agregamos dos medallas predeterminadas 
    medallas.agregar(lista_medallas[1])
    return medallas


        
