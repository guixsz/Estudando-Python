def retorna_antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


def soma(numeros):

    return sum(numeros)

def func_3():
    
    return print("Olá mundo!")

def salvar_carro(marca, carro, ano, placa):
    return print(f"Carro inserido com sucesso! {marca}/{carro}/{ano}/{placa}")

def subtracao(numeros):
    for numero in numeros:
      resultado = numero - numero
      return resultado

print(soma([2, 5, 10]))
print(retorna_antecessor_sucessor(2))
func_3()
salvar_carro("BMW", "x1", 2022, "123-432")
print(subtracao([40, 10]))