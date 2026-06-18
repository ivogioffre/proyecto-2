import json 

class Pokemon():
    def __init__(self,id,nombre,tipo,pc):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.pc = pc
    def __repr__(self):
         return f"{self.id} - {self.nombre} - Tipo: {self.tipo} - PC: {self.pc}"
        

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





        
