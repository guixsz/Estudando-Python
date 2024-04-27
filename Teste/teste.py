Valor_salario = int(input("Digite o seu salário: "))
valor_beneficio = int(input("Digite o valor do benefício: "))

valor_imposto = 0

if Valor_salario <= 1100:
    valor_imposto = 0.05 * Valor_salario
elif Valor_salario <= 2500:
    valor_imposto = 0.10 * Valor_salario
else:
    valor_imposto = 0.15 * Valor_salario

saida = Valor_salario - valor_imposto + valor_beneficio
print(f"Seu salário mensal é: {saida}")