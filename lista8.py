import re
def ex1():
    x = float(input('Insira o primeiro número da operação: '))
    while True:
        inputoperacao = input('''Insira a operação que deseja realizar com o próximo número:
        [SOMA]: Digite "+"
        [MULTIPLICAÇÃO]: Digite "x"
        [DIVISÃO]: Digite "/"
        [SUBTRAÇÃO]: Digite "-"

        ''')
        operadorespossiveis = (('-'),('+'),('x'),('/'))
        if inputoperacao not in operadorespossiveis:
            print('Operação inválida! Insira alguma das opções da lista: ')
            continue
        else: break
    y = float(input('Insira o segundo número da operação: '))
    soma = lambda x,y: x + y
    multiplica = lambda x,y: x*y
    subtrai = lambda x,y: x-y
    divide = lambda x,y: x/y
    if inputoperacao == '+':
        print(soma(x,y))
    elif inputoperacao == '-':
        print(subtrai(x,y))
    elif inputoperacao == 'x':
        print(multiplica(x,y))
    else: print(divide(x,y))

def ex2():
    estoque = [] #nessa matriz produtos cada produto é uma linha, sendo cada coluna uma característica do produto
    def cadastrarmercadoria():
        produto = []
        codigo = int(input('Insira o código do produto: '))#0
        descricao = str(input('Insira a descrição do produto: '))#1
        quantidade = int(input('Insira o quantidade do produto: '))#2
        precounitario = float(input('Insira o preço unitário do produto: ')) #3
        produto = [codigo,descricao,quantidade,precounitario]
        estoque.append(produto)

        
    def consultarmercadoria():
        codetosearch = int(input('Insira o código do produto a ser buscado no sistema:  ')) 
        for produto in estoque:
            if produto[0] == codetosearch:
                print(f'''O código procurado foi encontrado!
                descrição: {produto[1]},
                quantidade no estoque: {produto[2]}
                preço atual: {produto[3]}''')
            else:
                print('Produto não encontrado, verifique o código digitado.')
    def valortotal():
        somatotal = 0
        for i  in range(len(estoque)):
            somaproduto = estoque[i][2] * estoque[i][3]
            somatotal += somaproduto
        print(f' O valor total do estoque é {somatotal}')
    #opção de menu
    while True:
        option = int(input('''Insira a opção desejada:
        [1] - Cadastrar mercadoria
        [2] - Consultar mercadoria
        [3] - Valor total em mercadorias
        [4] - Sair
        >>>
        
        '''))
        if option == 4:
            break
        elif option ==1:
            cadastrarmercadoria()
        elif option ==2:
            consultarmercadoria()
        elif option ==3:
            valortotal()
        else: 
            print('Opção inválida!')
            continue


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