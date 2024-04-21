matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])
print(matriz[0][0])
print(matriz[1][2])
print(matriz[0][-1])

lista = ["p", "y", "t", "h", "o", "n"]
python = ["Python"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])
print(python[::-1])

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

numeros = [1, 2, 3, 4, 5, 30, 21, 9,65]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(numero)

n = [2, 4, 6, 9, 11, 15, 20, 30, 35]
p1 = [n2 for n2 in n if n2 % 2 == 1]
print(p1)


m1 = [1,30, 21, 2, 9, 65, 34]
quadrado = [m2 ** 2 for m2 in m1]
print(quadrado)