"""
3- Calculadora de Desconto em Produto
Desenvolva um programa que aplica um desconto sobre o preço de um produto. O programa deve:

* Solicitar o preço original do produto.  
* Solicitar o percentual de desconto desejado.  
* Calcular e exibir o preço final com desconto, arredondado para duas casas decimais.
"""
try:
    valor_produto = float(input("Digite o valor da produto: "))
    porc_desconto = float(input("Digite o valor da porcentagem do desconto (somente números): "))
    valor_desconto = valor_produto * porc_desconto / 100

    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Total a pagar (com desconto): R$ {valor_produto - valor_desconto:.2f}") 

except ValueError:
    print("Erro: Você deve digitar apenas números válidos (use ponto no lugar da vírgula, ex: 100.50).")