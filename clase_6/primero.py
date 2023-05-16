personas = [
  {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25
  },
  {
    "nombre": "Maria",
    "apellido": "Gonzalez",
    "edad": 30
  },
]



# archivo = open("prueba1.txt", "w")
# datos = "Hola mundo !!!"
# archivo.write(datos)
# archivo.close()

# with open("prueba1.txt", "w") as archivo:
#   datos = "Hola mundo con with !!!"
#   archivo.write(datos)

with open("prueba1.txt", "r") as archivo:
  datos = archivo.read()
  print(datos.upper())


