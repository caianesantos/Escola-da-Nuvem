"""
4- Leitura e Escrita de Arquivo JSON  
Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON. Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo. Para isso:

* Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).  
* Solicite ao usuário o nome do arquivo JSON.  
* Salve os dados no arquivo usando o módulo `json`.  
* Após salvar, leia o mesmo arquivo e imprima os dados carregados.  
* Trate possíveis erros como ausência do arquivo ou problemas na escrita.

Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.

---
"""

import json
import os

def salvar_e_ler_json():
    dados_pessoa = {
        "nome": "Caiane Santos",
        "idade": 23,
        "cidade": "Salvador"
    }

    nome_arquivo = input("Digite o nome do arquivo JSON (ex: dados_pessoa.json): ").strip()
    if not nome_arquivo.lower().endswith('.json'):
        nome_arquivo += '.json'

    try:
        # Salvar dados no arquivo JSON
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados_pessoa, f, ensure_ascii=False, indent=4)
        print(f" Dados salvos com sucesso no arquivo '{nome_arquivo}'.")

        # Ler e mostrar os dados do arquivo JSON
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            dados_lidos = json.load(f)
        print(" Conteúdo lido do arquivo JSON:")
        print(dados_lidos)

    except FileNotFoundError:
        print(f" Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except IOError as e:
        print(f" Erro de entrada/saída: {e}")
    except json.JSONDecodeError:
        print(" Erro ao decodificar o arquivo JSON — arquivo possivelmente corrompido.")
    except Exception as e:
        print(f" Erro inesperado: {e}")

if __name__ == "__main__":
    salvar_e_ler_json()
