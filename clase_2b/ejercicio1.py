
from models import Datos
from models import Producto
from models import Clasificacion

clasificaciones = [
  Clasificacion(1, 'Limpieza'),
  Clasificacion(2, 'Alimentos'),
  Clasificacion(3, 'Bebidas'),
  Clasificacion(4, 'Hogar')
]

datos:Datos = Datos(clasificaciones, [])

for clas in datos.getClasificaciones():
  print(clas)

print("idclasificacion 2: ", datos.leerClasificacion(2))
datos.agregarClasificacion(Clasificacion(5, 'Electrodomesticos'))

clas = datos.leerClasificacion(5)
datos.eliminarClasificacion(clas)


for clas in datos.getClasificaciones():
  print(clas)