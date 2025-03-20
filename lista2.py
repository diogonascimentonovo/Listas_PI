

#1
def ex1():
  velocidade = int(input('Qual a velocidade do veículo em km/h? '))
  if velocidade > 80:
    kmexcedido = velocidade - 80
    multa = 5 * kmexcedido
    print(f'Você foi multado em R${multa}')
  else:
    print('Velocidade regular')

#2
def ex2():
  numero = list(map(int, input('Insira os números separados por espaço (ex: 1 2 3): ').split()))
  menor = min(numero)
  maior = max(numero)
  print(f'o menor número é {menor}, e o maior é {maior}')

#3
def ex3():
  salario = float(input('Insira o seu salário: R$:'))
  if salario > 1250.00:
    aumento = salario * 1.10
  else:
    aumento = salario * 1.15

  print(f'Seu novo salário com aumento é de R$ {aumento:.2f}')

#4
def ex4():
  distancia = float(input('Qual a distância que deseja percorrer?'))
  if distancia < 200:
    preco = distancia * 0.45
  else: preco = distancia * 0.5
  print(preco)

#5
def ex5():
  numeros = list(map(float,input('insira dois números separados por espaço (ex: 1.4 6.7): ').split()))
  if len(numeros) != 2:
    print('Insira apenas 2 números.')
    return
  operacao = int(input('''Qual operação deseja realizar?
  [1]Soma(+)
  [2]Subtração(-)
  [3]Multiplicação(x)
  [4]Divisão( / ) 
  '''))
  if operacao == 1:
    resultado = sum(numeros)
  elif operacao == 2:
    resultado = numeros[0]- numeros[1]
  elif operacao == 3:
    resultado = numeros[0]*numeros[1]
  elif operacao == 4:
    resultado = numeros[0]/numeros[1]
  print(resultado)

#6
def ex6():
  valorcasa = float(input('Insira o valor da casa: '))
  salario = float(input('Qual o seu salário? '))
  quantidadeanos = int(input('Qual a quantidade de anos que deseja financiar? '))

  # Verifica se a entrada do valor da casa ou do salário é válida
  if valorcasa <= 0 or salario <= 0 or quantidadeanos <= 0:
    print("Erro: O valor da casa, salário e anos devem ser positivos.")
    return

  quantidademeses = quantidadeanos * 12
  parcela = valorcasa / quantidademeses

  # Verifica se a parcela excede 30% do salário
  if parcela > salario * 0.3:
    print(f'O valor da parcela ({parcela:.2f}) supera 30% do seu salário. '
          'Insira uma quantidade de anos maior ou um valor menor para a casa.')
    return
  else:
    print(f'O valor da parcela é de R$ {parcela:.2f}')



#7
def ex7():
  qtde = int(input('qual a quantidade em kWh consumida?'))
  while True:
    intl = str(input('''Qual o tipo de instalação?
    [R]Residencial
    [I]Industrial
    [C]Comercial
    ''').upper())
    if intl in ['R','I','C']:
      break
    else:
      print('Esse tipo de instalação não existe, insira novamente.')
  if intl =='R':
    if qtde <= 500:
      valor = qtde * 0.4
    else:
      valor = qtde * 0.65

  elif intl == 'I':
    if qtde <= 5000:
      valor = qtde * 0.55
    else:
      valor = qtde * 0.6

  elif intl == 'C':
    if qtde <= 1000:
      valor = qtde * 0.55
    else:
      valor = qtde * 0.6

  print(f'O valor da conta de energia é {valor:.2f}')



exercicioescolhido = int(input('Digite o número do exercício que quer rodar: (exemplo: 1) '))
listadeexercicios = {
    1: ex1,
    2: ex2,
    3: ex3,
    4: ex4,
    5: ex5,
    6: ex6,
    7: ex7

}

if exercicioescolhido in listadeexercicios:
    listadeexercicios[exercicioescolhido]()
else:
    print('Exercício não encontrado.')
