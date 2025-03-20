#ex 1
soma = 7.5 + 4.5 + 9
media = soma / 3
print(media)
#resultado 7.0

#ex 2
ladoemmetros= 350
area = ladoemmetros**2
print(area, "metros")
#resultado 122500 metros

#ex 3
raioemcm = 5
pi = 3.14159
area = pi * raioemcm**2
print(area, "centímetros quadrados")
#resultado 78.53975 centímetros quadrados

#ex 4
string1 = "Hugo"
string2 = "gastou 50 reais"
string3 = "ontem"
somadasstrings = (string1 +" "+ string2 +" "+ string3)
print(somadasstrings)
#resultado Hugo gastou 50 reais ontem

#ex 5
altura = float(input('Digite a altura: '))
base = float(input('Digite a base: '))
area = altura * base/2
print(area)


#ex 6
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
n3 = float(input('Digite mais um valor: '))
n4 = float(input('Digite o ultimo valor: '))
media = (n1 + n2 + n3 + n4) / 4
print(media)


#ex 7
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
produto = n1 * n2
print(produto)

#ex 8
ano_de_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_de_nascimento
idadeem2040=2040-ano_de_nascimento
print("você tem {} anos e em 2040 terá {} anos.".format(idade, idadeem2040))

#ex 9
quadrado_de_10 = 10**2
cubo_de_3 =3**3
resto_da_divisao = 1000%3.5
print("o quadrado de 10 é = {}, e o cubo de 3 é = {}, e o resto da divisão de 1000 por 5 é= {}".format(quadrado_de_10, cubo_de_3, resto_da_divisao))

#ex 10
comprimento_da_sala = float(input("Insira o comprimento da sala: "))
largura_da_sala = float(input("Insira o largura da sala: "))
area = largura_da_sala * comprimento_da_sala
print("A área da sala é {} metros quadrados".format(area))


#ex 11
conta = float(input("Digite o valor da conta: "))
gorjeta = conta * 10/100
contaegorjeta = conta + gorjeta
print('O valor da conta é {}, a gorjeta ficou {}, caso queira pagar o total é de {}'.format(conta,gorjeta,contaegorjeta))
