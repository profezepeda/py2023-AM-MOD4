from models.modelsClass import Curso, Alumno, Profesor

def cargarAlumnos() -> list:
  retorno = []
  retorno.append(Alumno("1-1", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("1-2", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("1-3", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("1-4", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("1-5", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("1-6", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("1-7", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("1-8", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("1-9", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("1-k", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("2-1", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("2-2", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("2-3", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("2-4", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  retorno.append(Alumno("2-5", "Juan", "Pablo", "Perez", "Perez", 20, 2020))
  return retorno

def cargarCursos():
  profe_mate = Profesor("1-1", "Juan", "Pablo", "Perez", "Perez", "matemáticas")
  lista_alumnos = cargarAlumnos()
  retorno = []
  retorno.append(Curso(nombre="1A"))
  retorno.append(Curso(nombre="2A", profesor=profe_mate))
  retorno.append(Curso(nombre="3A", alumnos=lista_alumnos, profesor=None))
  return retorno