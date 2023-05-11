class Ejemplo():

  def metodo_args(self, *args):
    print(args)
    for arg in args:
      print(arg)

  def metodo_kwargs(self, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
      print(f"{key}: {value}")


ejemplo = Ejemplo()
ejemplo.metodo_args("primero", "segundo", "tercero")
ejemplo.metodo_kwargs(nombre="Juan", apellido="Perez", edad=25)


