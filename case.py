# caso 1

def funcion1():
  return "Caso 1"

def funcion2():
  return "Caso 2"

def funcion3():
  return "Caso 3"

switch_diccionario = {
  "caso1": funcion1,
  "caso2": funcion2,
  "caso3": funcion3
}

resultado = switch_diccionario["caso1"]()
print(resultado)

# caso 2
match "caso1":
  case "caso1":
    print("Caso 1")
  case "caso2":
    print("Caso 2")
  case "caso3":
    print("Caso 3")
  case _:
    print("Caso no encontrado")