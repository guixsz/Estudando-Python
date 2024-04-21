linguagens = ["python", "js", "c"]
print(linguagens)

# Extender a lista com os objetos desejados

linguagens.extend(["java", "csharp"])
linguagens.extend(["php", "Typescript"])

print(linguagens)

# Método index() para buscar o índice do objeto descrito no parâmetro 

print(linguagens.index("java"))
print(linguagens.index("python"))
print(linguagens.index("csharp"))

# Método pop() para buscar o ultimo objeto presente na lista

print(linguagens.pop())
print(linguagens.pop())


# Remove() um objeto da lista

linguagens.remove("c")
print(linguagens)

# Reverte a ordem dos objetos da lista

linguagens.reverse()
print(linguagens)

# Ordena os objetos da forma que você quiser

linguagens.sort()
print(linguagens)

# Mostra o tamanho da lista

print(len(linguagens))
