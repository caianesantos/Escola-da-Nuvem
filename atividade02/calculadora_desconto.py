"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_produto = "camiseta"
preco_original = 50.00
preco_desconto = preco_original * 20 / 100

print(f"O valor do produto {nome_produto} é: R$ {preco_original:.2f}. Com desconto é: R${preco_desconto:.2f}")