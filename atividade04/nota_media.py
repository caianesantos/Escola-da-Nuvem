"""
2- Registro de Notas e Cálculo da Média
Desenvolva um programa para registrar notas de uma turma e calcular a média final. Siga as instruções abaixo:

* O programa deve solicitar notas continuamente até o usuário digitar "fim".  
* Somente notas entre 0 e 10 devem ser aceitas.  
* Ao final, exiba a média da turma com duas casas decimais e o total de notas válidas registradas.  
* Trate entradas inválidas com mensagens de erro.  
"""

notas = []  

while True:
    try:
        nota = float(input("Digite uma nota: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número real válido.")
        continue
    if nota > 10 or nota < 0:
        print("Digite uma nota válida.")
    else:
        notas.append(nota)
    
    continuar = input("Deseja continuar? (fim para não/ qualquer tecla para sim): ")
    if continuar == "fim":
        print(notas)
        if notas == []:
            print("Você precisa digitar uma nota.")
        else:
            soma = sum(notas)
            quantidade_notas = len(notas)
            media = soma / quantidade_notas
            print(f"Total de notas registradas: {quantidade_notas}")
            print(f"Média da turma: {media:.2f}")
        break