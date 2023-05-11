class Motor():
  tipo: str
  serie: str
  caracteristicas: str

  def __init__(self, tipo, serie, caracteristicas):
      self.tipo = tipo
      self.serie = serie
      self.caracteristicas = caracteristicas

class Automovil():
  color: str
  marca: str
  modelo: str
  anno: str
  ruedas: int
  motor: Motor

  def __init__(self, color, marca, modelo, anno, ruedas, motor):
    self.color = color
    self.marca = marca
    self.modelo = modelo
    self.anno = anno
    self.ruedas = ruedas
    self.motor = motor
  
  def encender(self):
    pass

  def apagar(self):
    pass
  
  def avanzar(self):
    pass
  
  def retroceder(self):
    pass
  
  def detener(self):
    pass

class AutoCombustion(Automovil):
  octanos: int
  rendimiento: float
  capacidad_estanque: int

  def __init__(self, color, marca, modelo, anno, ruedas, motor, octanos, rendimiento, capacidad_estanque):
    super().__init__(color, marca, modelo, anno, ruedas, motor)
    self.octanos = octanos
    self.rendimiento = rendimiento
    self.capacidad_estanque = capacidad_estanque
  
  def avanzar():  # sobreescribir el método avanzar
    pass

class AutoElectrico(Automovil):
  capacidad_bateria: int
  tiene_carga_rapida: bool
  autonomia: int
  
  def __init__(self, color, marca, modelo, anno, ruedas, motor, capacidad_bateria, tiene_carga_rapida, autonomia):
    super().__init__(color, marca, modelo, anno, ruedas, motor)
    self.capacidad_bateria = capacidad_bateria
    self.tiene_carga_rapida = tiene_carga_rapida
    self.autonomia = autonomia
  
  def avanzar(): # sobreescribir el método avanzar
    pass