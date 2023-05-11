direccion = ('Norte', 'Noreste', 'Este', 'Sureste', 'Sur', 'Suroeste', 'Oeste', 'Noroeste')

class Persona():
  rut: str = ""
  primer_nombre: str = ""
  segundo_nombre: str = ""
  primer_apellido: str = ""
  segundo_apellido: str = ""
  edad: int = 0
  __estado_civil: str = "Soltero/a"
  __esta_trabajando: bool = False
  __mirando_hacia: int = 0

  # def __init__(self, rut, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, edad):
  #   self.rut = rut
  #   self.primer_nombre = primer_nombre
  #   self.segundo_nombre = segundo_nombre
  #   self.primer_apellido = primer_apellido
  #   self.segundo_apellido = segundo_apellido
  #   self.edad = edad

  def __init__(self, **kwargs):
    if len(kwargs) == 0:
      print("No puede crear personas sin datos.  En este momento se ha creado una persona con datos vacíos.")
    elif len(kwargs) == 1 and "rut" in kwargs:
      print("Buscando en la base datos la persona con rut", kwargs["rut"])
      self.rut = kwargs["rut"]
      self.primer_nombre = "María"
      self.primer_apellido = "González"
      self.edad = 25
    else:
      self.rut = kwargs["rut"] if "rut" in kwargs else ""
      self.primer_nombre = kwargs["primer_nombre"] if "primer_nombre" in kwargs else ""
      self.segundo_nombre = kwargs["segundo_nombre"] if "segundo_nombre" in kwargs else ""
      self.primer_apellido = kwargs["primer_apellido"] if "primer_apellido" in kwargs else ""
      self.segundo_apellido = kwargs["segundo_apellido"] if "segundo_apellido" in kwargs else ""
      self.edad = kwargs["edad"] if "edad" in kwargs else 0

  def __str__(self):
    return f"{self.primer_nombre} {self.primer_apellido} - trabajando? {self.__esta_trabajando} - mirando hacia {direccion[self.__mirando_hacia]}"

  @property
  def esta_trabajando(self):
    return self.__esta_trabajando

  def mirando_hacia(self):
    return str(direccion[self.__mirando_hacia])

  def comenzar_a_trabajar(self):
    self.__esta_trabajando = True

  def dejar_de_trabajar(self):
    self.__esta_trabajando = False

  def girar(self, **kwargs):
    """ pasos: int """
    """ orientacion: str """
    pasos_ = 1 if "pasos" not in kwargs else kwargs["pasos"]
    if "orientacion" in kwargs:
      if kwargs["orientacion"] == "izquierda":
        pasos_ = pasos_ * -1
    self.__mirando_hacia += pasos_
    if self.__mirando_hacia == len(direccion):
      self.__mirando_hacia = 0
    if self.__mirando_hacia < 0:
      self.__mirando_hacia = len(direccion) - 1


juanito:Persona = Persona(rut="12345678-9", primer_nombre="Juan", segundo_nombre="Pablo", 
                          primer_apellido="Perez", segundo_apellido="Gonzalez", edad=25)
juanito.girar(pasos=3, orientacion="izquierda")
print(juanito)
juanito.girar()
print(juanito)
juanito.comenzar_a_trabajar()
print(juanito)

maria:Persona = Persona(rut="1-9")
maria.girar(pasos=15, orientacion="izquierda")
print(maria)

otro:Persona = Persona()
otro.primer_nombre = "Otro"
otro.primer_apellido = "Apellido"
print(otro)

parametros = { "rut": "2-7", "primer_nombre": "Nueva", "primer_apellido": "Persona" }
nuevo:Persona = Persona(**parametros)
print("Nuevo", nuevo)


# print(juanito)
# juanito.comenzar_a_trabajar()
# print(juanito)
# juanito.dejar_de_trabajar()
# print(juanito)

# for vueltas in range(0, 5):
#   juanito.girar()
#   donde_mira = juanito.mirando_hacia()
#   print(donde_mira)

# maria:Persona = Persona(edad=30, rut="12345678-9", primer_nombre="Maria", segundo_nombre="Paz", primer_apellido="Gonzalez", segundo_apellido="Perez")
# print(maria)