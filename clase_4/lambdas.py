suma = lambda x, y: x + y
print(suma(2, 3))

multiplicacion = lambda x, y: x * y
print(multiplicacion(2, 3))

print(multiplicacion(suma(2, 3), 4))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros)
print(pares)

resultado = list(map(lambda x: 2**x, numeros))
print(resultado)