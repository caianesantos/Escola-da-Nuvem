"""
1- Gerador de Senhas Seguras  
Crie um programa que gera senhas aleatórias com letras, números e caracteres especiais. Siga as instruções abaixo:

* Solicite ao usuário o tamanho da senha desejada (por exemplo: 8, 12, 16 caracteres).  
* A senha gerada deve conter letras maiúsculas, minúsculas, números e símbolos (ex: !@#$%&*).  
* Exiba a senha gerada ao final do programa.  

Dica: Use os módulos `random` e `string` para gerar os caracteres aleatórios.
"""

import random
import string

def gerar_senha (tamanho):
    if tamanho < 4:
        print("Erro: a senha deve ter no mínimo 4 caracteres.")
        return

    letra_minuscula = random.choice(string.ascii_lowercase)
    letra_maiuscula = random.choice(string.ascii_uppercase)
    numero = random.choice(string.digits)
    simbolo = random.choice(string.punctuation)

    senha_base = [letra_minuscula, letra_maiuscula, numero, simbolo]

    # tamanho = int(input("Digite o tamanho que deseja: "))

    caracteres = string.ascii_letters + string.digits + string.punctuation

    restante = random.choices(caracteres, k=tamanho - 4)


    senha_base += restante
    random.shuffle(senha_base)
    senha_final = ''.join(senha_base)
    return senha_final

solicitar_tamanho = int(input("Digite o tamanho desejado: "))
senha = gerar_senha(solicitar_tamanho)
if senha:
    print("Senha gerada:", senha)