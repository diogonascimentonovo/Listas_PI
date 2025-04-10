import re
def ex1():
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    def funcao():
        num = (n1,n2)
        return num
    num = funcao()
    print(f'O maior número é {max(num)}')
def ex2():
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    resultado = 0
    def funcao(n1,n2):
        if n2 % n1:
            return True
        else: return False
    retorno = funcao(n1,n2)
    print(retorno)
def ex3():
    base = int(input('Insira a medida da base do triângulo: '))
    altura = int(input('Insira a altura do triângulo: '))
    def area(altura,base):
        return (base*altura)/2
    print(f'A área do triângulo é {area(altura,base)}')
def ex4(): 
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    dois = (n1,n2)
    opcao = int(input('''Escolha a operação que deseja fazer com os números:
    [1] SOMA
    [2] SUBTRAÇÃO
    [3] MULTIPLICAÇÃO
    [4] DIVISÃO                                                           '''))
    def soma(dois):
        return n1 + n2
    def subtracao(dois):
        return n1-n2
    def multiplicacao(dois):
        return n1*n2
    def divisao(dois):
        return n1/n2
    if opcao == 1:
        print(soma(dois))
    elif opcao == 2:
        print(subtracao(dois))
    elif opcao == 3:
        print(multiplicacao(dois))
    elif opcao == 4:
        print(divisao(dois))
def ex5():
    a = int(input('Insira o número a: '))
    b = int(input('Insira o número b: '))
    def mdc(a,b):
        vetor = []
        for i in range(1,a):
            if a % i == 0 and b % i == 0:
                vetor.append(i)
        return max(vetor)    
    print(f'O MDC de {a} e {b} é {mdc(a,b)}')
def ex6():
    matriza = []
    matrizb = []
    for 
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