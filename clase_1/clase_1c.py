class Producto():
  __nombre:str = None
  marca: str = None
  __precio:int = None
  __impuesto:int = 0.19

  @property
  def nombre(self):
    return self.__nombre
  
  @property
  def precio(self):
    return self.__precio
  
  @precio.setter
  def precio(self, precio):
    self.__precio = precio
  
  @property
  def iva(self):
    return self.__impuesto

  def __init__(self, nombre, marca, precio):
    self.__nombre = nombre
    self.marca = marca
    self.__precio = precio
  
  def valor_bruto(self):
    return self.precio + (self.__precio * self.__impuesto)


producto = Producto('Coca Cola', 'Coca Cola',1000)
producto2 = Producto('Pepsi', 'Pepsi', 1000)


print(producto.nombre, producto.marca, producto.precio)
producto.marca = "Coca Cola Co."
print(producto.nombre, producto.marca, producto.precio)

print(producto.iva)
