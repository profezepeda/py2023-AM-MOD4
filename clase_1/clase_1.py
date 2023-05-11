class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f'Hola, mi nombre es {self.nombre} y tengo {self.edad} años')


persona_juan = Persona('Juan', 25)
persona_juan.saludar()
persona_maria = Persona('Maria', 30)
persona_maria.saludar()

persona_jose:Persona = None
print(persona_jose)
persona_jose = Persona('Jose', 35)
print(persona_jose)

persona_mario:Persona = Persona('Mario', 40)

personas = [
  persona_juan,
  persona_maria,
  persona_jose,
  Persona("Mario",40),
  Persona("Luis",45),
  Persona("Ana",50)
]

print(personas)

