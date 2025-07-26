"""
1- Calculadora de Gorjeta
Crie um programa que calcula o valor da gorjeta a partir do total da conta e da porcentagem escolhida. Use as instruções abaixo:

* Defina o valor da conta (ex: R$ 100,00).  
* Informe a porcentagem da gorjeta (ex: 10%, 15%, 20%).  
* O programa deve calcular o valor correspondente e exibir o resultado com duas casas decimais. 
"""
try:
    valor_conta = float(input("Digite o valor da conta: "))
    porc_gorjeta = float(input("Digite o valor da porcentagem (somente números): "))
    valor_gorjeta = valor_conta * porc_gorjeta / 100

    print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")
    print(f"Total a pagar (conta + gorjeta): R$ {valor_conta + valor_gorjeta:.2f}")

except ValueError:
    print("Erro: Você deve digitar apenas números válidos (use ponto no lugar da vírgula, ex: 100.50).")