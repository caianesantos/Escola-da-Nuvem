"""
3- Verificador de Senhas Fortes
Crie um programa que avalia a força de uma senha informada pelo usuário. O programa deve:

* Solicitar a senha até que o usuário digite "sair".  
* Verificar se a senha possui pelo menos 8 caracteres.  
* Verificar se contém pelo menos um número.  
* Informar se a senha é fraca ou forte.  
* Encerrar o programa apenas quando a senha for forte ou se o usuário digitar "sair".  
"""
while(True):
    senha = input("Digite sua senha (A senha deve conter: \n pelo menos 8 caracteres; \n pelo menos um número.): ")
    if senha == "sair":
        break
    elif len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte.")
        break
    else:
        print("Senha fraca")