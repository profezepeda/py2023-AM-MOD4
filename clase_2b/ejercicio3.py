from models import Marca


marca1 = Marca()
marca1.idmarca = 1
marca1.marca = "Pepsi"
marca2 = Marca(2, "Coca Cola")
marca3 = Marca()
marca4 = Marca(idmarca=4, marca="Fanta")

print(marca1)
print(marca2)
print(marca3)
print(marca4)