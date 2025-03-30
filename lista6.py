
def ex1():
    matriz = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]
    n = int(input('Insira a linha que deseja visualizar os valores: '))
    print(matriz[n-1])

def ex2():
    matriz = []
    for i in range(8):
        linhas = []
        for j in range(8):   
            linhas.append(j+1)
    matriz.append(linhas)
    for linhas in matriz:
        print(linhas)
        
                
    

def ex3(): print("Executando exercício 3!")

def ex4(): print("Executando exercício 4!")

def ex5(): print("Executando exercício 5!")

def ex6(): print("Executando exercício 6!")


totalex = int(input('Insira o total de exercícios: '))

# Criando a biblioteca automaticamente
biblioteca = {i: globals()[f"ex{i}"] for i in range(1, totalex + 1)}

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
