"""
4- Conversor de Moedas (para Reais - BRL)  
Crie um programa que mostra a cotação atual de moedas estrangeiras em relação ao Real. O programa deve:

* Solicitar ao usuário o código da moeda estrangeira (ex: USD, EUR, GBP).  
* Acessar a API: "https://economia.awesomeapi.com.br/last/{moeda}-BRL".  
* Exibir a cotação atual, o valor máximo, o valor mínimo e a data/hora da última atualização.  
* Informar ao usuário se o código da moeda for inválido ou houver falha na conexão.  

Dica: A conversão da data/hora pode ser feita com o módulo `datetime`.
"""
import requests as r
from datetime import datetime

def converter_moeda():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()

    if not moeda.isalpha() or len(moeda) != 3:
        print("Código inválido. Digite exatamente 3 letras, como USD, EUR, GBP.")
        return

    try:
        retorno = r.get(f"https://economia.awesomeapi.com.br/last/{moeda}-BRL")

        if retorno.status_code == 200:
            dados = retorno.json()

            chave = moeda + "BRL"

            if chave in dados:
                info = dados[chave]

                cotacao = info["bid"]
                maximo = info["high"]
                minimo = info["low"]
                timestamp = int(info["timestamp"])
                
                data_hora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

                print(f"Cotação atual do {moeda} em BRL:")
                print(f"Valor atual: R$ {cotacao}")
                print(f"Valor máximo: R$ {maximo}")
                print(f"Valor mínimo: R$ {minimo}")
                print(f"Última atualização: {data_hora}")

            else:
                print("Moeda não encontrada ou código inválido.")    

        else:
            print(f"Erro no código da moeda ou ao acessar a API. Código: {retorno.status_code}")
    except r.exceptions.RequestException as e:
        print("Erro de conexão:", e)

converter_moeda()