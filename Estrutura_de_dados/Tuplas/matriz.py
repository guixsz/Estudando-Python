matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

print(matriz[0])
print(matriz[0][0])
print(matriz[0][-1])
print(matriz[-1][-1])

# Fatiamento da tupla 

tupla = ("p", "y", "t", "h", "O", "n")

print(tupla[2:])
print(tupla[:2])
print(tupla[1:3])
print(tupla[0:3:2])
print(tupla[::])
print(tupla[::-1], end="\n")

# laços de repetição for com tuplas

carros = ("gol", "celta", "palio\n")

for carro in carros:
    print(carro)

# Enumerate com tuplas

c1 = ("Hyundai", "Nissan", "Amarok")

for indice, c1s in enumerate(c1):
    print(f"{indice}: {c1s}")