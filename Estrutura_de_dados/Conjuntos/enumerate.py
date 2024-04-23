carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# método Union

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_c = conjunto_a.union(conjunto_b)

print(conjunto_c)

# Método de intersecção

print(conjunto_a.intersection(conjunto_b))

# Diferença

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# Simétrica

print(conjunto_a.symmetric_difference(conjunto_b))

# Issubset

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

# issuperset

print(conjunto_b.issuperset(conjunto_a))
print(conjunto_b.issuperset(conjunto_a))

# Add, ignora um objeto já existente

sorteio = {1, 23}

sorteio.add(25)
sorteio.add(45)

print(sorteio)

# Método clear()

# sorteio.clear()

print(sorteio)

# discard(), discarta um valor do conjunto

sorteio.discard(45)

print(sorteio)

# pop(), remove um objeto da lista de forma crescente

sorteio.pop()

print(sorteio)

# remove(), remove um valor do conjunto, diferença dele pro discard é que se remover um produto que n exite da erro,

sorteio.remove(25)
print(sorteio)

# len(), tira o tamanho do conjunto

print(len(sorteio))
