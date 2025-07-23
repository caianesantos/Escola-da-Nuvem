"""
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. 
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

# Caso 1) É um número divisível por 4, mas não é divisível por 100.
# Caso 2) É um número divisível por 4, por 100 e por 400.

ano = int(input("Digite um ano para verificar se é ou não bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0):
    print(f"O ano {ano} é bissexto.") 

else:
    print(f"O ano {ano} não é bissexto.") 
