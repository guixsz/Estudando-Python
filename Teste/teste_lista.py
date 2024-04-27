itens = []

for i in range(3):
    item = input("Digite o nome do item {}: " .format(i + 1))
    itens.append(item)


print("Lista de itens:")
for item in itens:
    print(f"- {item}")