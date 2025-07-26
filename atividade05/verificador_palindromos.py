"""
2- Verificador de Palíndromos
Crie um programa que verifica se uma palavra ou frase é um palíndromo, ou seja,
se pode ser lida da mesma forma de trás para frente, desconsiderando espaços, acentos e pontuação. Para isso:

*Solicite ao usuário uma palavra ou frase.
*Desconsidere letras maiúsculas, espaços e sinais de pontuação.
*Verifique se a frase é um palíndromo.
*Exiba "Sim" se for palíndromo ou "Não" se não for.

Exemplo: A frase "A cara rajada da jararaca" deve ser reconhecida como um palíndromo.
"""
import re 

palavra_frase = input("Digite uma palavra ou frase: ")

corrigida = re.sub(r'[^a-zA-Z0-9]', '', palavra_frase).lower()
print(corrigida)

if corrigida == corrigida[::-1]:
    print("É palíndromo.")
else:
    print("Não é palíndromo.")