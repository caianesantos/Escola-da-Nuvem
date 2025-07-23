"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f"Seu peso é: {peso}. \n Sua altura é: {altura}. \n Seu IMC é: {imc:.2f}. \n Portanto, sua classificação é: abaixo do peso.")
elif imc > 18.5 and imc <= 25:
    print(f"Seu peso é: {peso}. \n Sua altura é: {altura}. \n Seu IMC é: {imc:.2f}. \n Portanto, sua classificação é: peso normal.")
elif imc > 25 and imc <= 30:
    print(f"Seu peso é: {peso}. \n Sua altura é: {altura}. \n Seu IMC é: {imc:.2f}. \n Portanto, sua classificação é: sobrepeso.")
else:
    print(f"Seu peso é: {peso}. \n Sua altura é: {altura}. \n Seu IMC é: {imc:.2f}. \n Portanto, sua classificação é: obeso.")

    