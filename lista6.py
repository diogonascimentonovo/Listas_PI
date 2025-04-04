import re
import random
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
        linhasa = []
        for j in range(3):
            linhasa.append(int(input(f'Insira o elemento da matriz A: ({i+1},{j+1}): ')))
        matrizA.append(linhasa)
    matrizB = []
    for i in range(5):
        linhasb = []
        for j in range(3):
            linhasb.append(int(input(f'Insira o elemento da matriz B: ({i+1},{j+1}): ')))
        matrizB.append(linhasb)
    matrizC = []
    for i in range(5):
        linhasc= []
        for j in range(3):
            linhasc.append((matrizA[i][j])*(matrizB[i][j]))
        matrizC.append(linhasc)
    print('A matriz C é: ')
    for linhasc in matrizC:
        print(linhasc)

def ex4():
    matrizA = []
    for i in range(6):
        linhasa = []
        for j in range(6):
            if {i+1} == {j+1}:
                linhasa.append(10)
            else:
                linhasa.append(int(input(f'Insira o elemento da matriz A: ({i+1},{j+1}): ')))
        matrizA.append(linhasa)
    for linhasa in matrizA:
        print(linhasa)
    
def ex5():
    matriz = []
    while True:
        n = int(input('Insira quantas linhas deseja na matriz: '))
        if n<1:
            print('A quantidade de linhas deve ser pelo menos 1! ')
            continue
        else: break
    while True:
        m = int(input('Insira quantas coluna deseja na matriz: '))
        if m<1:
            print('A quantidade de colunas deve ser pelo menos 1! ')
            continue
        else: break
    for i in range(n):
        linhas = []
        for j in range(m):
            linhas.append(random.randint(1,10))
        matriz.append(linhas)
    for linhas in matriz:
        print(linhas)
    numeroprocurado = int(input('Insira o número que deseja procurar na matriz (de 0 a 10): '))
    encontrado = False
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == numeroprocurado:
                print(f'Encontrado na posição {i}, {j}')
                encontrado = True
    if not encontrado:     
        print('Não encontrado')

def ex6():
    va = []
    vb = []
    for i in range(12): 
        va.append(random.randint(1,10))
        vb.append(random.randint(1,10))
    print(f' o vetor A é: {va},e o vetor B é: {vb}')
    for i in range(len(va)):
        va[i] = va[i]*2
    for i in range(len(vb)):
        vb[i] = vb[i]-2
    
    mc = [] 
    for i in range(12):
        linhas = [va[i], vb[i]]
        mc.append(linhas)
    print('A matriz C é: ')
    for linhas in mc:
        print(linhas)
    
globals_copy = globals().copy()
biblioteca = {}
for name, obj in globals_copy.items():
    match = re.findall(r"^ex(\d+)$", name)
    if match and callable(obj):
        biblioteca[int(match[0])] = obj

while True:
    select = int(input('Selecione o exercício que deseja rodar (ou 0 para sair): '))
    
    if select == 0:
        print("Saindo...")
        break

    if select in biblioteca:
        biblioteca[select]()  
    else:
        print('Exercício não encontrado')
