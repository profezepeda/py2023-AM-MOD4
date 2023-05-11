from models.modelsClass import Curso


class CursoView():
  __lista_cursos: list = []

  def __init__(self, lista_cursos):
    self.__lista_cursos = lista_cursos
  
  def listar(self):
    print("LISTA CURSOS ***************")
    if len(self.__lista_cursos) == 0:
      print("No hay cursos")
    for curso in self.__lista_cursos:
      if curso.profesor is not None:
        print(f"{curso.nombre} - {curso.profesor.primer_nombre} {curso.profesor.primer_apellido} - { len(curso.alumnos) } alumnos/as")
      else:
        print(f"{curso.nombre} - Sin profesor - { len(curso.alumnos) } alumnos/as")
    print("***********************************", end="\n\n\n")

  def asignarProfesor(self, lista_profesores) -> list:
    print("ASIGNAR PROFESOR/A A CURSO ***************")
    # Curso
    nombre = input("Ingrese el nombre del curso: ")
    curso_seleccionado: Curso = None
    for curso in self.__lista_cursos:
      if curso.nombre == nombre:
        curso_seleccionado = curso
        break
    if curso_seleccionado is None:
      print("No se encontró el curso")
      return self.__lista_cursos

    # Profesor/a
    for profe in lista_profesores:
      print(f"{profe.run} - {profe.primer_nombre} {profe.primer_apellido}")
    profesor = input("Ingrese el run del profesor: ")
    profesor_seleccionado = None
    for profe in lista_profesores:
      if profe.run == profesor:
        profesor_seleccionado = profe
        break
    if profesor_seleccionado is None:
      print("No se encontró el profesor")
      return self.__lista_cursos

    curso_seleccionado.profesor = profesor_seleccionado
    for elemento in self.__lista_cursos:
      if elemento.nombre == curso_seleccionado.nombre:
        elemento = curso_seleccionado

    print("***********************************", end="\n\n\n")
    return self.__lista_cursos