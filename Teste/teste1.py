quantidade_passos = int(input(""))

if quantidade_passos == 0:
    print("Nenhum passo dado na floresta.")

for passo in range(1, quantidade_passos + 1):

    if passo == 1:
        palavra_passo = "passo"
    else:
        palavra_passo = "passos"
    

    print("Explorador:", passo, palavra_passo)