class Clasificacion():
  idclasificacion: int
  clasificacion: str

  def __init__(self, idclasificacion, clasificacion):
    self.idclasificacion = idclasificacion
    self.clasificacion = clasificacion

  def __str__(self):
    return f"{self.idclasificacion} - {self.clasificacion}"


class Producto():
  idproducto: int
  proveedor: str
  marca: str
  nombre: str
  sku: str
  clasificacion: Clasificacion
  __stock: float
  __costopmp: float

  def __init__(self, idproducto, proveedor, marca, nombre, sku, clasificacion):
    self.idproducto = idproducto
    self.proveedor = proveedor
    self.marca = marca
    self.nombre = nombre
    self.sku = sku
    self.clasificacion = clasificacion
    self.__stock = 0
    self.__costopmp = 0

class Datos():
  __clasificaciones: list = []
  __productos: list = []
  
  def __init__(self, clasificaciones, productos):
    self.__clasificaciones = clasificaciones
    self.__productos = productos

  def getClasificaciones(self):
    return self.__clasificaciones

  def agregarClasificacion(self, clasificacion):
    self.__clasificaciones.append(clasificacion)

  def actualizarClasificacion(self, clasificacion):
    for clas in self.__clasificaciones:
      if clas.idclasificacion == clasificacion.idclasificacion:
        clas.clasificacion = clasificacion.clasificacion

  def eliminarClasificacion(self, clasificacion):
    for clas in self.__clasificaciones:
      if clas.idclasificacion == clasificacion.idclasificacion:
        self.__clasificaciones.remove(clas)

  def leerClasificacion(self, idclasificacion):
    for clas in self.__clasificaciones:
      if clas.idclasificacion == idclasificacion:
        return clas

class Menu():
  """ opciones = lista de diccionarios { "opcion": numero, "texto": string }"""
  __opciones: list = []

  def __init__(self, opciones):
    self.opciones = opciones

  def mostrar(self):
    for opcion in self.opciones:
      print(f"{opcion['opcion']}. {opcion['texto']}")
    while True:
      opcion = input("Ingrese una opción: ")
      if opcion.isnumeric():
        opcion = int(opcion)
        for op in self.opciones:
          if op["opcion"] == opcion:
            return opcion
    return None

class Marca():
  idmarca: int = None
  marca: str = None

  def __init__(self, *args, **kwargs):
    """ idmarca, marca """
    if len(args) == 1:
      self.idmarca = args[0]
    elif len(args) == 2:
      self.idmarca = args[0]
      self.marca = args[1]
    if "idmarca" in kwargs:
      self.idmarca = kwargs["idmarca"]
    if "marca" in kwargs:
      self.marca = kwargs["marca"]

  def __str__(self) -> str:
    return f"{self.idmarca} - {self.marca}"