"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o 
em uma das seguintes categorias: 

*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais).
"""

idade = float(input("Digite sua idade: "))

if idade <= 12:
    print(f"Sua idade é: {idade}, portanto você é criança.")
elif idade >12 and idade <= 17:
    print(f"Sua idade é: {idade}, portanto você é adolescente.")
elif idade >17 and idade <= 59:
    print(f"Sua idade é: {idade}, portanto você é adulto.")
else:
    print(f"Sua idade é: {idade}, portanto você é idoso.")
    
