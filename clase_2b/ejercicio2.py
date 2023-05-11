from models import Menu

opciones = [
  { "opcion": 1, "texto": "Agregar clasificacion" },
  { "opcion": 2, "texto": "Actualizar clasificacion" },
  { "opcion": 3, "texto": "Eliminar clasificacion" },
  { "opcion": 4, "texto": "Leer clasificacion" },
  { "opcion": 0, "texto": "Salir" }
]

menu = Menu(opciones)
seleccion = menu.mostrar()
if seleccion is None:
  print("No seleccionó una opción")
else:
  if seleccion == 1:
    opciones = [
      { "opcion": 1, "texto": "Opción 1" },
      { "opcion": 2, "texto": "Opción 2" },
      { "opcion": 3, "texto": "Opción 3" },
      { "opcion": 4, "texto": "Opción 4" }
    ]
    sub_menu = Menu(opciones)
    seleccion2 = sub_menu.mostrar()