def ex1():
  while True:
    try:
      numeros = list(map(float, input('Insira 5 números espaçados: ').split()))
      if len(numeros)!=5:
        print('Erro! é necessário inserir 5 números.')
        continue
      break
    except ValueError:
      print('Erro! é necessário inserir apenas números.')
      continue
  numeros = list(map(lambda x: x**2, numeros))
  print(numeros)
def ex2():
  for i in range (1,101):
    print(i)
def ex3():
  for i in range(100,0,-1):
    print(i)
def ex4():
  for i in range (10):
    print(2*(i+1))
def ex5():
  n = int(input('Insira um número para visualizar sua tabuada: '))
  for i in range(10):
    print((i+1) *n)
def ex6():
  soma = 0
  for i in range (1,101):
    soma +=i
  print(soma)
def ex7():
    while True:
        try:
            numero = int(input('Insira um numero inteiro e maior que 0: '))
            if numero <= 0:
                print('O número inserido é menor que 0.')
                continue
            break
        except ValueError:
            print('O número escolhido não é um inteiro!')
            continue
    n = 0
    exp = 2**n
    while exp < numero:
        print(exp, end=", "if exp* 2<= numero else "\n")
        exp *=2
def ex8():
  subtotal = 0
  while True:
    qtde = int(input('Insira a quantidade de produtos: '))
    if qtde == 0:
      break
    while qtde < 0:
      print('Erro! A quantidade de produtos não pode ser negativa.')
      qtde = int(input('Insira a quantidade de produtos: '))
    vlr = float(input('Insira o valor do produto: '))
    while vlr < 0:
      print('Erro! O valor do produto não pode ser negativo.')
      vlr = float(input('Insira o valor do produto: '))
    novoitem = qtde * vlr
    subtotal += novoitem
  print(f'O subtotal da compra é:R$ {subtotal:.2f}')
def ex9():
  x = int(input('Insira um valor para mostrar a sequencia de números inteiros positivos até o numero escolhido: '))
  for i in range(1, x):
    print(i, end=', ' if i+1 < x else '\n') 
biblioteca = {
    1: ex1,
    2: ex2,
    3: ex3,
    4: ex4,
    5: ex5,
    6: ex6,
    7: ex7,
    8: ex8,
    9: ex9,
}
while True:
  exercicioescolhido = int(input('Escolha um exercício: '))
  if exercicioescolhido not in biblioteca:
    print('Erro! Exercício não encontrado.')
  else:
    biblioteca[exercicioescolhido]()

