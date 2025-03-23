def ex1():
  notas = []
  for i in range(5):
    notas.append(float(input('Digite a nota: ')))
  print(f'A média das notas é {sum(notas)/len(notas)}')
def ex2():
  numeros = []
  for i in range(10):
    numeros.append(int(input('Digite um número')))
  maior = max(numeros)
  menor = min(numeros)
  locmaior = numeros.index(maior)
  locmenor = numeros.index(menor)
  print(f'O maior número é {maior} e está na posição {locmaior+1}')
  print(f'O menor número é {menor} e está na posição {locmenor+1}')
#esse exercício possui um problema no loop da tratativa de erro de localização de número e na localização dos números.
def ex3():
  vetor = []
  while True:
    try:
      numero = float(input('Insira um número para adicionar ao vetor, caso deseje parar de inserir digite uma letra: '))
      vetor.append(numero)
      continue
    except ValueError:
      break
  procurar = float(input('Insira o número que deseja buscar no vetor:'))
  if procurar in vetor:
    correspondencias = 0
    correspondencias = vetor.count(procurar)
    loc = vetor.index(procurar)
    print(f'Foram encontrados {correspondencias} correspondencias no vetor, localizadas nas posições {loc}.')
  else:
    procurar = float(input('numero não encontrado no vetor, por favor digite outro: '))

def ex4():
  vetorA = [1, 0, 5, -2, -5, 7]
  vetorB = [2, 3, 0, -7, 6, 8]
  vetorC = []
  vetorC = vetorA + vetorB
  print(f'Vetor C: {vetorC}')
def ex5():
  meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
  numeromeses = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
  for i in range(12):
    print(f'{numeromeses[i]} - {meses[i]}')

def ex6():
  notas = [float(input('Digite a nota do aluno: ')) for i in range(10)]
  media = sum(notas)/len(notas)
  maiorquemedia = [nota for nota in notas if nota > media]
  print(f'A média das notas é {media:.2f}')
  if maiorquemedia:
    print(f'No total são {len(maiorquemedia)} notas maior que a média')
def ex7():
  vetorA = [1, 0, 5, -2, -5, 7]
  vetorB = [2, 3, 0, -7, 6, 8]
  vetorC = []
  vetorC = [vetorA[i] * vetorB[i] for i in range(len(vetorA))]
  print(vetorC)
biblioteca = {
    1: ex1,
    2: ex2,
    3: ex3,
    4: ex4,
    5: ex5,
    6: ex6,
    7: ex7
}
while True:
  select = int(input('Selecione o exercício que deseja rodar: '))
  if select in biblioteca:
    biblioteca[select]()
  else:
    print('Exercício não encontrado')