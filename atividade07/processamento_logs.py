"""
1- Processamento de Logs de Treinamento  
Crie um programa que analisa um arquivo CSV contendo dados de execução de um processo de treinamento. O programa deve:

* Solicitar ao usuário o nome do arquivo CSV (ex: logs_treinamento.csv).  
* Ler os dados usando a biblioteca `pandas`.  
* Calcular a média e o desvio padrão da coluna `tempo_execucao`.  
* Exibir os resultados com duas casas decimais.  
* Tratar erros como arquivo inexistente ou formatação incorreta.

Dica: Use `df['coluna'].mean()` e `df['coluna'].std()` para obter os resultados estatísticos.

"""

import pandas as pd
import os

def analisar_logs_treinamento():
    """
    1- Processamento de Logs de Treinamento
    Analisa um arquivo CSV contendo dados de execução de um processo de treinamento.
    """
    try:
        nome_pasta = input("Digite o nome da pasta onde está o arquivo (ou pressione Enter se estiver na mesma pasta): ").strip()
        nome_arquivo = input("Digite o nome do arquivo csv (ex: logs_treinamento.csv): ").lower()

        if not nome_arquivo.endswith('.csv'):
            nome_arquivo += '.csv'

        caminho_completo = os.path.join(nome_pasta, nome_arquivo) if nome_pasta else nome_arquivo

        df = pd.read_csv(caminho_completo)
        coluna_alvo = 'tempo_execucao'

        if coluna_alvo not in df.columns:
            print(f"Erro de Formatação: A coluna '{coluna_alvo}' não foi encontrada no arquivo '{nome_arquivo}'.")
            print(f"Colunas disponíveis: {list(df.columns)}")
            return
        
        df[coluna_alvo] = pd.to_numeric(df[coluna_alvo], errors='coerce')
        df.dropna(subset=[coluna_alvo], inplace=True)

        if df.empty:
            print(f"Erro de Formatação: A coluna '{coluna_alvo}' não contém dados numéricos válidos.")
            return

        media = df[coluna_alvo].mean()
        desvio_padrao = df[coluna_alvo].std()

        print("--- Análise do Tempo de Execução ---")
        print(f"Média: {media:.2f}")
        print(f"Desvio Padrão: {desvio_padrao:.2f}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_completo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    analisar_logs_treinamento()
