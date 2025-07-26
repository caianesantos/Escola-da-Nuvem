"""
4- Calculadora de Idade em Dias
Crie um programa que calcula a idade aproximada de uma pessoa em dias. Para isso:

* Solicite o ano de nascimento da pessoa.  
* Considere o ano atual automaticamente.  
* Calcule a idade em anos e transforme em dias (desconsidere anos bissextos).  
* Exiba o resultado final.
"""
from datetime import datetime

try:
    data_nascimento = int(input("Digite a data em que você nasceu: "))
    mes_nascimento = int(input("Digite o mês em que você nasceu: "))
    ano_nascimento = int(input("Digite o ano em que você nasceu: "))

    data_nascimento = datetime(ano_nascimento, mes_nascimento, data_nascimento)
    data_atual = datetime.now()
    
    diferenca = data_atual - data_nascimento
    idade_em_dias = diferenca.days

    print(f"Data de nascimento: {data_nascimento.strftime('%d/%m/%Y')}")
    print(f"Data atual: {data_atual.strftime('%d/%m/%Y')}")
    print(f"Sua idade exata em dias é: {idade_em_dias} dias")

except ValueError:
    print("Data inválida! Por favor, digite valores numéricos corretos.")