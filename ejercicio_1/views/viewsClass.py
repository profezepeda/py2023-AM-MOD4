class Menu():
  """ opciones = lista de diccionarios { "opcion": numero, "texto": string }"""
  _opciones: list = []

  def __init__(self, opciones):
    self.opciones = opciones

  def mostrar(self):
    for opcion in self.opciones:
      print(f"{opcion['opcion']}. {opcion['texto']}")
    while True:
      opcion = input("Ingrese una opción: ")
      if opcion.isnumeric():
        opcion = int(opcion)
        for op in self.opciones:
          if op["opcion"] == opcion:
            return opcion
    return None

class subMenuProfesores(Menu):
  def __init__(self):
    opciones_gestion = [
      { "opcion": 1, "texto": "Listar Profesores/as" },
      { "opcion": 2, "texto": "Agregar Profesor/a" },
      { "opcion": 3, "texto": "Actualizar Profesor/a" },
      { "opcion": 4, "texto": "Eliminar Profesor/a" },
      { "opcion": 5, "texto": "Leer Profesor/a" },
      { "opcion": 0, "texto": "Volver" }
    ]
    super().__init__(opciones_gestion)

class subMenuAlumnos(Menu):
  def __init__(self):
    opciones_gestion = [
      { "opcion": 1, "texto": "Listar Alumnos/as" },
      { "opcion": 2, "texto": "Agregar Alumno/a" },
      { "opcion": 3, "texto": "Actualizar Alumno/a" },
      { "opcion": 4, "texto": "Eliminar Alumno/a" },
      { "opcion": 5, "texto": "Leer Alumno/a" },
      { "opcion": 0, "texto": "Volver" }
    ]
    super().__init__(opciones_gestion)

class subMenuCursos(Menu):
  def __init__(self):
    opciones_gestion = [
      { "opcion": 1, "texto": "Listar Cursos" },
      { "opcion": 2, "texto": "Asignar Profesor/a Curso" },
      { "opcion": 3, "texto": "Agregar Alumno/a a Curso" }
    ]
    super().__init__(opciones_gestion)