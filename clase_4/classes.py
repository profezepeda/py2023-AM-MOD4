from time import sleep


class Automovil():
  color: str
  marca: str
  modelo: str
  # motor: Motor
  _encendido: bool = False
  _velocidad: int = 0

  def __init__(self, color, marca, modelo):
    self.color = color
    self.marca = marca
    self.modelo = modelo

  def __str__(self):
    return f"Automovil {self.marca} {self.modelo} - encendido? {self._encendido}"

  @property
  def encendido(self):
    return self._encendido

  def encender(self):
    self._encendido = True

  def apagar(self):
    self._encendido = False

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

  def __init__(self, color, marca, modelo, octanos, rendimiento, capacidad_estanque):
    super().__init__(color, marca, modelo)
    self.octanos = octanos
    self.rendimiento = rendimiento
    self.capacidad_estanque = capacidad_estanque

  def encender(self):
    print("Pasar corriente al motor")
    print("Calentar bujias")
    print("Inyectar combustible")
    print("Encender motor")
    self._encendido = True
  
  def avanzar(self, velocidad):
    self._velocidad = velocidad
    print("Velocidad: ", end="", flush=True)
    for i in range(0, self._velocidad, 10):
      print("█"*10, end="", flush=True)
      sleep(0.5)
    print()
    print("Inyectar combustible")
    print(f"Avanzando a {self._velocidad} km/h")

  def __str__(self):
    return f"AutoCombustion {self.marca} {self.modelo} - encendido? {self.encendido}"

class AutoElectrico(Automovil):
  capacidad_bateria: int
  tiene_carga_rapida: bool
  autonomia: int

  def __init__(self, color, marca, modelo, capacidad_bateria, tiene_carga_rapida, autonomia):
    super().__init__(color, marca, modelo)
    self.capacidad_bateria = capacidad_bateria
    self.tiene_carga_rapida = tiene_carga_rapida
    self.autonomia = autonomia

  def encender(self):
    print("Pasar energía al motor")
    self._encendido = True

  def avanzar(self, velocidad):
    self._velocidad = velocidad
    print("Velocidad: ", end="", flush=True)
    for i in range(0, self._velocidad, 25):
      print("█"*25, end="", flush=True)
      sleep(0.5)
    print()
    print("Pasar más wattage al motor")
    print(f"Avanzando a {self._velocidad} km/h")

  def __str__(self):
    return f"AutoEletrico {self.marca} {self.modelo} - encendido? {self.encendido}"
