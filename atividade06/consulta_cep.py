"""
3- Consulta de CEP  
Desenvolva um programa que consulta dados de endereço a partir de um CEP brasileiro. Siga os passos abaixo:

* Solicite ao usuário que digite um CEP (apenas números, sem traço).  
* Acesse a API pública do ViaCEP: "https://viacep.com.br/ws/{cep}/json/".  
* Exiba as seguintes informações: logradouro, bairro, cidade, estado e o próprio CEP.  
* Caso o CEP não exista ou haja erro, informe isso de forma clara ao usuário.  

Dica: Use o módulo `requests` e trate exceções com `try/except`.
"""
import requests as r

def consultar_cep ():
    cep = input("Digite um cep (apenas números, sem traço): ").strip()

    if not (cep.isdigit() and len(cep) == 8):
        print("CEP inválido. Digite exatamente 8 números.")
        return
    
    try:
        retorno = r.get(f"https://viacep.com.br/ws/{cep}/json/")

        if retorno.status_code == 200:
            dados = retorno.json()

            if "erro" in dados:
                print("CEP não encontrado.")
            else:
                print("Logradouro:", dados.get("logradouro", "Não disponível"))
                print("Bairro:", dados.get("bairro", "Não disponível"))
                print("Cidade:", dados.get("localidade", "Não disponível"))
                print("Estado:", dados.get("uf", "Não disponível"))
                print("CEP:", dados.get("cep", "Não disponível"))
        else:
            print(f"Erro ao consultar o CEP. Código: {retorno.status_code}")

    except r.exceptions.RequestException as e:
        print("Erro de conexão:", e)


consultar_cep()