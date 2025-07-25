"""
1- Calculadora Simples
Crie um programa que simule uma calculadora básica com as seguintes funcionalidades:

* Solicite ao usuário dois números reais.  
* Peça a operação desejada (+, -, *, /).  
* Realize a operação escolhida e exiba o resultado.  
* Trate divisões por zero e operações inválidas com mensagens apropriadas.  

O programa deve continuar solicitando entradas até que uma operação válida seja realizada com sucesso.
"""
def soma (a,b):
    return a + b

def subtracao (a,b):
    return a - b

def multiplicacao (a,b):
    return a * b

def divisao (a,b):
    return a / b

while (True):
    try:
        numero1 = float(input("Digite 1° número: "))
        numero2 = float(input("Digite o 2° número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número real válido.")
        continue
    operacao = input("Digite o tipo de operação que deseja (+, -, *, /): ")
    
    if operacao in ["+", "-", "*", "/"]:
        if (operacao == "/") and (numero2 == 0):
            print("Operação inválida. A divisão não pode ser realizada.")
            continue
        elif operacao == "/": 
            print(f"A divisão de {numero1} / {numero2} = {divisao(numero1, numero2)}")
            break

        elif operacao == "+":
                print(f"A soma de {numero1} + {numero2} = {soma(numero1, numero2)}")
                break

        elif operacao == "-":
            print(f"A subtração de {numero1} - {numero2} = {subtracao(numero1, numero2)}")
            break

        elif operacao == "*":
            print(f"A multiplicação de {numero1} * {numero2} = {multiplicacao(numero1, numero2)}")
            break
    else:        
        print("Operação inválida. Tente novamente utilizando: +, -, * ou /.")






