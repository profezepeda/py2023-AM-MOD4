from controllers.dummy import cargarAlumnos, cargarCursos
from views.profesoresView import ProfesorView
from views.cursosView import CursoView
from views.viewsClass import Menu, subMenuProfesores, subMenuAlumnos, subMenuCursos
from models.modelsClass import Datos

datos = Datos()
datos.alumnos = cargarAlumnos()
datos.cursos = cargarCursos()

opciones = [
  { "opcion": 1, "texto": "Gestionar Profesores" },
  { "opcion": 2, "texto": "Gestionar Alumnos" },
  { "opcion": 3, "texto": "Gestionar Cursos" },
  { "opcion": 0, "texto": "Salir" },
]

menu:Menu = Menu(opciones)
while True:
  opcion_principal = menu.mostrar()
  if opcion_principal is None or opcion_principal == 0:
    break
  elif opcion_principal == 1:
    vista = ProfesorView(datos.profesores)
    while True:
      sub_menu_profesores = subMenuProfesores()
      opcion_sub_menu = sub_menu_profesores.mostrar()
      if opcion_sub_menu is None or opcion_sub_menu == 0:
        break
      elif opcion_sub_menu == 1:
        vista.listar()
      elif opcion_sub_menu == 2:
        datos.profesores = vista.agregar()
      elif opcion_sub_menu == 3:
        datos.profesores = vista.actualizar()
      elif opcion_sub_menu == 4:
        datos.profesores = vista.eliminar()
      elif opcion_sub_menu == 5:
        vista.mostrar()
  elif opcion_principal == 2:
    while True:
      sub_menu_alumnos = subMenuAlumnos()
      opcion_sub_menu = sub_menu_alumnos.mostrar()
      if opcion_sub_menu is None or opcion_sub_menu == 0:
        break
  elif opcion_principal == 3:
    vista = CursoView(datos.cursos)
    while True:
      sub_menu_cursos = subMenuCursos()
      opcion_sub_menu = sub_menu_cursos.mostrar()
      if opcion_sub_menu is None or opcion_sub_menu == 0:
        break
      elif opcion_sub_menu == 1:
        vista.listar()
      elif opcion_sub_menu == 2:
        datos.cursos = vista.asignarProfesor(datos.profesores)

print("Gracias por usar el sistema")