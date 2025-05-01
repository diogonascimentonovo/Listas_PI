import re
def ex1():
    lista1 = input('Insira a primeira lista: ')
    lista2 = input('Insira a segunda lista: ')
    lista3 = lista1 + lista2
    print(f'A lista 3 é: {lista3}')


def ex2():
    lista1 = input('Insira a primeira lista: ')
    lista2 = input('Insira a segunda lista: ')
    lista3 = set(lista1 + lista2)
    print(lista3)

def ex3():
    try:
        with open('pares.txt', 'r') as arquivospares:
            pares = [int(linha.strip()) for linha in arquivospares if linha.strip().isdigit()]
        with open('impares.txt', 'r') as arquivosimpares:
            impares = [int(linha.strip()) for linha in arquivosimpares if linha.strip().isdigit()]
        
        total = pares + impares
        total.sort()

        with open('total.txt', 'w') as arquivoresultado:
            for numero in total:
                arquivoresultado.write(f'{numero}\n')

        print(f'\nFeito! Arquivo total.txt criado!\n\nConteúdo do arquivo:')
        
        with open('total.txt', 'r') as arquivoresultado:
            for linha in arquivoresultado:
                print(linha.strip())

    except FileNotFoundError as e:
        print(f"Erro: {e}. Você precisa criar 'pares.txt' e 'impares.txt' primeiro!")

def ex4():
    try:
        with open('pares.txt', 'r') as arquivospares:
            pares = [int(linha.strip()) for linha in arquivospares if linha.strip().isdigit()]
        with open('impares.txt', 'r') as arquivosimpares:
            impares = [int(linha.strip()) for linha in arquivosimpares if linha.strip().isdigit()]
        total = pares + impares
        total.sort(reverse = True)
        with open('total.txt', 'w') as arquivoresultado:
            for numero in total:
                arquivoresultado.write(f'{numero}\n')

        print(f'\nFeito! Arquivo total.txt criado!\n\nConteúdo do arquivo:')
        
        with open('total.txt', 'r') as arquivoresultado:
            for linha in arquivoresultado:
                print(linha.strip())

    except FileNotFoundError as e:
        print(f"Erro: {e}. Você precisa criar 'pares.txt' e 'impares.txt' primeiro!")

def ex5():
    nomes = input("Digite os nomes separados por espaço: ").split()
    nomes.sort()
    with open("nomes.txt", "w") as arquivo:
        for nome in nomes:
            arquivo.write(f"{nome}\n")
    print("Arquivo criado com sucesso!")


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