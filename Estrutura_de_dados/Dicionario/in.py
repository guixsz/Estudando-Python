contatos = {
    "guilherme@exemplo.com": {"nome": "Guilherme Santana", "idade": 20, "telefone": "3313-2425"},
    "giovanna@exemplo.com": {"nome": "Giovanna Castilho", "idade": 22, "telefone": "98765-5125"},
    "melaine@exemplo.com": {"nome": "Melaine Santos", "idade": 25, "telefone": "3882383294"}
}

resultado = "alexsandro@exemplo.com" in contatos
print(resultado)

resultado = "idade" in contatos["guilherme@exemplo.com"]
print(resultado)