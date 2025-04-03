import re

def ex1():
    matriz = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]
    n = int(input('Insira a linha que deseja visualizar os valores: '))
    print(matriz[n-1])

def ex2():
    matriz = []

    print('Insira os elementos da matriz 8x8: ')
    for i in range(8):
        linha = []
        for j in range(8):
            linha.append(int(input(f"Elemento ({i+1},{j+1}): ")))
        matriz.append(linha)

    soma_diagonal = 0
    for i in range(8):
        soma_diagonal += matriz[i][i]
    print(f"A soma dos elementos da diagonal principal é: {soma_diagonal}")
    print(f"A soma dos elementos da diagonal principal é: {soma_diagonal}")    

def ex3(): 
    matrizA = []
    for i in range(5):
        linhas = []
        for j in range(3):
            linhas.append(int(input(f'Insira o elemento {i+1}, {j+1}: ')))
    matrizA.append(linhas)
    for linhas in matrizA:
        print(matrizA)


def ex4(): print("Executando exercício 4!")

def ex5(): print("Executando exercício 5!")

def ex6(): print("Executando exercício 6!")

# Obtendo todas as funções que seguem o padrão ex1, ex2, ex3...
globals_copy = globals().copy()
biblioteca = {}
for name, obj in globals_copy.items():
    match = re.findall(r"^ex(\d+)$", name)
    if match and callable(obj):
        biblioteca[int(match[0])] = obj
# Loop para selecionar e rodar exercícios
while True:
    select = int(input('Selecione o exercício que deseja rodar (ou 0 para sair): '))
    
    if select == 0:
        print("Saindo...")
        break

    if select in biblioteca:
        biblioteca[select]()  # Chama a função correspondente
    else:
        print('Exercício não encontrado')
