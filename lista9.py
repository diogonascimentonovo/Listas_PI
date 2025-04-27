import re
def ex1():
    string1 = str(input('Insira a primeira String: '))
    string2 = str(input('Insira a segunda string: '))
    busca = string1.find(string2)
    if  busca != 0:
        print('Encontrado!')
        print(f'{string2} Encontrado na posição {busca} da primeira string')
    else: print('Nâo encontrado!')
                
def ex2():
    str1 = str(input('Insira a primeira string: '))
    str2 = str(input('Insira a segunda string: '))
    comum = set()
    for letras in str1:
        if letras in str2:
            comum.add(letras)
    print(f'As letras em comum são: {comum}')
#Verificar qual tipo de armazenamento de dado não armaezena duplicados para que seja melhor nesse exercício

def ex3():
    str1 = str(input('Insira a primeira string: '))
    str2 = str(input('Insira a segunda string: '))
    resultado = set()
    for item in str1:
        if item not in str2 and item not in resultado:
            resultado.add(item)
    for iten in str2:
        if iten not in str1 and iten not in resultado:
            resultado.add(iten)
    print(resultado)


def ex4():
    str1 = str(input('Insira a string: '))
    letras = set(str1)
    for item in letras:
        print(f'{item}: {str1.count(item)}x ')
        

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