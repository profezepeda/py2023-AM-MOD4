from classes import Automovil, AutoCombustion, AutoElectrico

# auto_generico = Automovil("rojo", "mazda", "3")
# print(auto_generico)
# auto_generico.encender()
# print(auto_generico)
# auto_generico.apagar()
# print(auto_generico)

auto_combustion = AutoCombustion("rojo", "mazda", "3", 95, 12.5, 45)
print(auto_combustion)
auto_combustion.encender()
print(auto_combustion)
auto_combustion.avanzar(50)
print(auto_combustion)

auto_electrico = AutoElectrico("rojo", "Tesla", "XYZ", 45, True, 120)
print(auto_electrico)
auto_electrico.encender()
print(auto_electrico)
auto_electrico.avanzar(50)
print(auto_electrico)
