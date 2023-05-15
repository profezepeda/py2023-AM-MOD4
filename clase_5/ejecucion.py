from excepciones import ValorNoAdminisibleException

class Calculo:
  def dividir(self, dividendo, divisor):
    if divisor <= 0:
      raise ValorNoAdminisibleException(divisor)
    return dividendo / divisor


calcular = Calculo()
try:
  resultado = calcular.dividir(100, 5)
  print("Primer resultado: ", resultado)

  resultado = calcular.dividir(100, 0)
  print("Segundo resultado: ", resultado)
except ValorNoAdminisibleException as e:
  print(e)