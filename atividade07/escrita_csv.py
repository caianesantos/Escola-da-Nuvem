"""
2- Escrita de Arquivo CSV  
Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV. Para isso:

* Crie uma lista de listas com dados fictícios de pelo menos três pessoas.  
* Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.  
* Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.  
* Confirme a gravação exibindo uma mensagem com o nome do arquivo.  
* Trate possíveis erros de escrita de arquivo.

Dica: Use `csv.writer()` para escrever os dados linha por linha.
"""


import csv
import os

def salvar_dados_csv():
    """
    2- Escrita de Arquivo CSV
    Escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV.
    """
    cabecalho = ['nome', 'idade', 'cidade']
    dados_pessoas = [
        ['Ana Silva', 28, 'Salvador'],
        ['Bruno Costa', 45, 'Lauro de Freitas'],
        ['Carla Dias', 33, 'Camaçari'],
        ['Daniel Farias', 22, 'Feira de Santana']
    ]

    try:
        pasta_destino = "atividade07"
        os.makedirs(pasta_destino, exist_ok=True)

        nome_arquivo = input("Digite o nome do arquivo para salvar (ex: pessoas.csv): ")
        if not nome_arquivo.lower().endswith('.csv'):
            nome_arquivo += '.csv'

        caminho_completo = os.path.join(pasta_destino, nome_arquivo)

        with open(caminho_completo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow(cabecalho)
            escritor_csv.writerows(dados_pessoas)

        print(f" Sucesso! Os dados foram gravados no arquivo '{caminho_completo}'.")

    except IOError as e:
        print(f"Erro de E/S: Não foi possível escrever no arquivo '{nome_arquivo}'.")
        print(f"Verifique se você tem permissão para escrever neste local.")
        print(f"Detalhes do erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    salvar_dados_csv()
