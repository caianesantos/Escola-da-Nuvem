"""
2- Gerador de Usuário Aleatório  
Crie um programa que acessa uma API pública e exibe informações de um usuário fictício. Para isso:

* Use a API pública "https://randomuser.me/api/" para obter dados aleatórios.  
* Mostre na tela: nome completo, e-mail e país do usuário.  
* O programa deve tratar possíveis erros de conexão ou falha na API.  

Dica: Utilize o módulo `requests` para fazer a requisição e o método `.json()` para acessar os dados.
"""
import requests as r

def gerar_usuario ():
    try:
        retorno = r.get("https://randomuser.me/api/")

        if retorno.status_code == 200:
            dados = retorno.json()

            usuario = dados["results"][0]
            nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
            email = usuario["email"]
            pais = usuario["location"]["country"]

            print("Nome:", nome)
            print("E-mail:", email)
            print("País:", pais)
        
        else:
            print(f"Erro ao acessar a API. Código: {retorno.status_code}")
    except r.exceptions.RequestException as e:
        print("Erro de conexão:", e)


gerar_usuario()
    
