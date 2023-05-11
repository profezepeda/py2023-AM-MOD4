class Persona:
  nombre: str = ''
  edad: int = 0

  def __init__(self, **kwargs):
    if "nombre" in kwargs:
      self.nombre = kwargs["nombre"]
    if "edad" in kwargs:
      self.edad = kwargs["edad"]
  
  def __str__(self):
    return f'Nombre: {self.nombre}, Edad: {self.edad}'

  def saludar(self):
    print(f'Hola a todas y todos, mi nombre es {self.nombre} y tengo {self.edad} años')

persona_juan = Persona()
persona_juan.nombre = 'Juan'
persona_juan.edad = 25
persona_juan.saludar()
persona_maria = Persona()
persona_maria.nombre = 'María'
persona_maria.edad = 30
persona_maria.saludar()

persona_jose: Persona = Persona(nombre="José", edad=35)
persona_jose.saludar()
print(persona_jose)

personas = [
  persona_juan,
  persona_maria,
  persona_jose,
  Persona(nombre="Mario", edad=40),
  Persona(nombre="Luis", edad=45),
  Persona(nombre="Ana", edad=50)
]

print(personas)