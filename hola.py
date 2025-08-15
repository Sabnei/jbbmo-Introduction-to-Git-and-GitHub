print("hola desde mi casa")


edad = 24 #Prueba de git

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")
    
    def cumplir_anios(self):
        self.edad += 1
    
    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"