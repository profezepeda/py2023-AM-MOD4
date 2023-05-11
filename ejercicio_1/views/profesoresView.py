from models.modelsClass import Profesor


class ProfesorView():
  __lista_profesores: list = []

  def __init__(self, lista_profesores):
    self.__lista_profesores = lista_profesores

  def listar(self):
    print("LISTA PROFESORES/AS ***************")
    if len(self.__lista_profesores) == 0:
      print("No hay profesores/as")
    for profesor in self.__lista_profesores:
      print(f"{profesor.run} - {profesor.primer_nombre} {profesor.primer_apellido}")
    print("***********************************", end="\n\n\n")

  def agregar(self) -> list:
    print("AGREGAR PROFESOR/A ***************")
    run = input("Ingrese el run: ")
    primer_nombre = input("Ingrese el primer nombre: ")
    segundo_nombre = input("Ingrese el segundo nombre: ")
    primer_apellido = input("Ingrese el primer apellido: ")
    segundo_apellido = input("Ingrese el segundo apellido: ")
    especialidad = input("Ingrese la especialidad: ")
    self.__lista_profesores.append(Profesor(run, primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, especialidad))
    print("***********************************", end="\n\n\n")
    return self.__lista_profesores

  def eliminar(self) -> list:
    print("ELIMINAR PROFESOR/A ***************")
    run = input("Ingrese el run: ")
    for profesor in self.__lista_profesores:
      if profesor.run == run:
        self.__lista_profesores.remove(profesor)
    print("***********************************", end="\n\n\n")
    return self.__lista_profesores

  def actualizar(self) -> list:
    profesor: Profesor = None
    print("MODIFICAR PROFESOR/A ***************")
    run = input("Ingrese el run: ")
    for elemento in self.__lista_profesores:
      if elemento.run == run:
        profesor = elemento
    if profesor is None:
      print("No se encontró el profesor/a")
      return self.__lista_profesores

    profesor.primer_nombre = input(f"Primer nombre [ {profesor.primer_nombre} ]: ")
    profesor.segundo_nombre = input(f"Segundo nombre [ {profesor.segundo_nombre} ]: ")
    profesor.primer_apellido = input(f"Primer apellido [ {profesor.primer_apellido} ]: ")
    profesor.segundo_apellido = input(f"Segundo apellido [ {profesor.segundo_apellido} ]: ")
    profesor.especialidad = input(f"Especialidad [ {profesor.especialidad} ]: ")
    print("***********************************", end="\n\n\n")
    for elemento in self.__lista_profesores:
      if elemento.run == run:
        elemento = profesor
    return self.__lista_profesores

  def mostrar(self):
    print("MOSTRAR PROFESOR/A ***************")
    run = input("Ingrese el run: ")
    for profesor in self.__lista_profesores:
      if profesor.run == run:
        print(f"Run: {profesor.run}")
        print(f"Nombre: {profesor.primer_nombre} {profesor.segundo_nombre} {profesor.primer_apellido} {profesor.segundo_apellido}")
        print(f"Especialidad: {profesor.especialidad}")
        break
    print("***********************************", end="\n\n\n")
