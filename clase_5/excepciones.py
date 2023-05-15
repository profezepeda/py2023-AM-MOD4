class ValorNoAdminisibleException(Exception):
  def __init__(self, valor):
    self.valor = valor

  def __str__(self):
    return f'El valor {self.valor} no es admisible, debe ser mayor a cero'