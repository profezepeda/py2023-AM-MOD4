def sumar():
  resultado = 0
  while True:
    try:
      numero1 = input("Ingrese un número (ingrese cualquier otro caracter para salir): ")
      resultado += int(numero1)
    except:
      break
  print(resultado)

def division(valor1, valor2):
  try:
    return valor1 / valor2
  except ZeroDivisionError:
    return "No se puede dividir por cero"


# sumar()

# valor1 = 100
# valor2 = 0
# while  True:
#   valor_input = input("Ingrese un valor: ")
#   if valor_input.isnumeric():
#     valor2 = int(valor_input)
#     break
#   else:
#     print("Ingrese un valor numérico")
# print("RESULTADO SUMA:", valor1 + valor2)
# print("RESULTADO RESTA:", valor1 - valor2)
# print("RESULTADO MULTIPLICACIÓN:", valor1 * valor2)
# print("RESULTADO DIVISIÓN: ", end="")
# print(division(valor1, valor2))

def cien_divido(valor):
  try:
    if valor < 0:
      raise ValueError("El valor no puede ser negativo")
    return 100 / valor
  except ZeroDivisionError:
    return "No se puede dividir por cero"
  except TypeError:
    return "No se puede dividir por un string"

serie = [1, 2, 3, 4, 5, 0, 6, "hola", 7, 8, 9, 10, -1, -6]
for valor in serie:
  print(f"para valor 100/{valor}: ", end="")
  try:
    # abrir
    print(cien_divido(valor), end=" -> ")
    # cerrar
  except ValueError as e:
    print(e, end=" -> ")
  finally:
    print(" OK ")