import json 

class Pokemon():
    def __init__(self,id,nombre,tipo,pc):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.pc = pc
    def __repr__(self):
         return f"{self.id} - {self.nombre} - Tipo: {self.tipo} - PC: {self.pc}"
        

