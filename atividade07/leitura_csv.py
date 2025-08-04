"""
3- Leitura de Arquivo CSV  
Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela. Para isso:

* Solicite ao usuário o nome do arquivo CSV a ser lido.  
* Utilize o módulo `csv` para abrir o arquivo e ler os dados.  
* Exiba cada linha completa como uma lista.  
* Trate erros como arquivo inexistente ou problemas na leitura.

Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.

"""

"""
3- Leitura de Arquivo CSV
Lê os dados de um arquivo CSV e imprime cada linha como uma lista.
"""

import csv
import os

def ler_arquivo_csv():
    arquivo = input("Digite o nome do arquivo a ser lido: ")
    if not arquivo.lower().endswith('.csv'):
        arquivo += '.csv'

    pasta_arquivo = input("Digite qual é a pasta do arquivo: ")
    caminho_completo = os.path.join(pasta_arquivo, arquivo)

    try:
        with open(caminho_completo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
            leitura = csv.reader(arquivo_csv)
            linhas = list(leitura)

            if not linhas:
                print(" O arquivo está vazio.")
                return

            print(" Conteúdo do arquivo:")
            for linha in linhas:
                print(linha)

    except FileNotFoundError:
        print(f" Erro: O arquivo '{caminho_completo}' não foi encontrado.")
    except Exception as e:
        print(f" Ocorreu um erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    ler_arquivo_csv()
