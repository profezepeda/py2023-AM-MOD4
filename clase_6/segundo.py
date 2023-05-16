import json

# configuracion = None
# with open("configuracion.json") as config:
#   data = config.read()
#   configuracion = json.loads(data)

# print(configuracion)

# personas = []
with open("personas.json", "r") as archivo:
  datos = archivo.read()
  personas = json.loads(datos)

# personas.append({
#   "nombre": "Jose",
#   "apellido": "Ramos",
#   "edad": 39
# })
# print(personas)

for persona in personas:
  if persona["nombre"] == "Jose":
    persona["edad"] = 40
    break

for persona in personas:
  if persona["nombre"] == "Juan":
    personas.remove(persona)
    break

with open("personas.json", "w") as archivo:
  datos = json.dumps(personas)
  archivo.write(datos)

print(personas)

