pessoa = {"Nome": "Guilherme", "Idade": 28}

pessoa = dict(nome="Guilherme", idade=28)

print(pessoa)

pessoa["nome"] = "Maria"
pessoa["idade"] = 18

print(pessoa)

# Matriz em dicionário

contatos = {
    "guilherme@exemplo.com": {"nome": "Guilherme Santana", "idade": 20, "telefone": "3313-2425"},
    "giovanna@exemplo.com": {"nome": "Giovanna Castilho", "idade": 22, "telefone": "98765-5125"},
    "melaine@exemplo.com": {"nome": "Melaine Santos", "idade": 25, "telefone": "3882383294"}
}

print(contatos["guilherme@exemplo.com"]["nome"])
print(contatos["melaine@exemplo.com"]["telefone"])

for chave, valor in contatos.items():
    print(chave, valor)


for chave in contatos:
    print(chave, contatos[chave])


# Método clear(), Apaga todos os valores do dicionário

# contatos.clear()

#print(contatos)


copia = contatos.copy()

print(copia)

# Adicionar novas chaves de uma vez só com o msm valor no seu dicionário

novas_chaves = dict.fromkeys(["nome", "telefone"], "Vazio")

print(novas_chaves)

# O método get retorna

print(contatos.get("chave", {}))
print(contatos.get("guilherme@exemplo.com", {}))

# O método pop() remove um valor passado como parâmetro do dicionario

contatos.pop("guilherme@exemplo.com")

print(contatos)

# O método popitem() remove a ultima chave do dicionário, sem precisar usar parâmetro

contatos.popitem()
print(contatos)