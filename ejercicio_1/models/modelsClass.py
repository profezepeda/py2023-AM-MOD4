class Persona():
  run: str
  primer_nombre: str
  segundo_nombre: str
  primer_apellido: str
  segundo_apellido: str

  def __init__(self, run, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
    self.run = run
    self.primer_nombre = primer_nombre
    self.segundo_nombre = segundo_nombre
    self.primer_apellido = primer_apellido
    self.segundo_apellido = segundo_apellido

class Alumno(Persona):
  edad: int
  matricula: int

  def __init__(self, run, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, edad, matricula):
    super().__init__(run, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido)
    self.edad = edad
    self.matricula = matricula

class Profesor(Persona):
  especialidad: str
  __sueldo: int = 0

  def __init__(self, run, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, especialidad):
    super().__init__(run, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido)
    self.especialidad = especialidad

class Curso():
  nombre: str
  alumnos: list = []
  profesor: Profesor = None

  def __init__(self, **kwargs):
    if "nombre" in kwargs:
      self.nombre = kwargs["nombre"]
    if "profesor" in kwargs:
      self.profesor = kwargs["profesor"]
    if "alumnos" in kwargs:
      self.alumnos = kwargs["alumnos"]

  # def __init__(self, nombre, alumnos, profesor):
  #   self.nombre = nombre
  #   self.alumnos = alumnos
  #   self.profesor = profesor


class Datos():
  profesores: list = []
  alumnos: list = []
  cursos: list = []