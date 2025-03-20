#ex1
def ex1():
    idade = int(input('Insira sua idade: '))
    while idade <=0:
        idade = int(input('Idade Inválida, digite novamente sua idade: '))
    if idade >= 65:
        print('Você tem mais de 65 anos')
    elif idade>= 18:
            print('Você é maior de idade')
    else:print('você é menor de idade')
#ex2
def ex2():
    salario = float(input(f'insira seu salario: '))
    while salario <=0:
        salario = float(input('Salário inválido,insira seu salario: '))
    if salario <=600:
        print('Não há desconto sobre seu salario')
    elif salario < 600 and salario <= 1200:
        desconto = salario *0.2
        print(f'O seu desconto do INSS é de {desconto:.2f}')
    elif salario > 1200 and salario <= 2000:
        desconto = salario*0.25
        print(f'O seu desconto do INSS é de {desconto:.2f}')
    else:
        desconto = salario * 0.3
        print(f'O seu desconto é de {desconto:.2f}')
#ex3
def ex3():
    primeiro_numero = int(input('Insira o primeiro número: '))
    segundo_numero = int(input('Insira o segundo número: '))
    if primeiro_numero + segundo_numero >10:
        print(f'A soma dos valores é {primeiro_numero + segundo_numero}')
    else: print('Os valores somados não são maiores que 10')
#ex4
def ex4():
    primeiro_numero = int(input('Insira o primeiro número: '))
    segundo_numero = int(input('Insira o segundo número: '))
    if primeiro_numero + segundo_numero >= 10:
        soma = primeiro_numero + segundo_numero + 5
    else:
        soma = primeiro_numero + segundo_numero - 7
    print(f'O números digitados foram {primeiro_numero} e {segundo_numero} e o resultado da operação foi {soma}')
#ex5
def ex5():
    numeros = list(map(int, input('Insira 3 números diferentes espaçados: ').split()))
    while len(numeros)!=3 or len(set(numeros)) != 3:
        numeros = list(map(int, input('Insira apenas 3 números diferentes separados por espaço: ').split()))
    numeros.sort()
    print(numeros[2])
#ex6
def ex6():
    idade = int(input('Insira a idade do nadador: '))
    while idade < 5:
        idade = int(input('Insira uma idade válida(A partir de 5 anos)'))
    #Infantil A
    if idade >= 5 and idade <=7:
        print('A categoria do nadador é Infantil A')
    #Infantil B
    elif idade >= 8 and idade <=11:
            print('A categoria do nadador é Infantil B')
    #Juvenil A
    elif idade >=12 and idade <=13:
        print('A categoria do nadador é Juvenil A')
    #Juvenil B
    elif idade >=14 and idade <=17:
        print('A categoria do nadador é Juvenil B')
    #Adultos
    else:
        print('A categoria do nadador é Adultos')
#ex7
def ex7():
    media = float(input('Insira a média do aluno: '))
    if media >= 7:
        print('Aluno aprovado!')
    elif media >=4 and media <7:
        print('O aluno irá para o exame final')
    else:
        print('Aluno reprovado')
#ex8
def ex8():
    salario = float(input('Insira seu salário bruto: '))
    if salario <= 600:
        print(f'Não há desconto do INSS, salário bruto é R$:{salario:.2f}, o desconto do INSS é R$:0.00 e o seu salário líquido é R$:{salario:.2f}')
    elif salario > 600 and salario <= 1200:
        desconto = salario*0.2
        salarioliq = salario - desconto
        print(f'O salário bruto é R$:{salario:.2f} o desconto é de R$:{desconto:.2f} e o salário líquido é R$:{salarioliq:.2f} ')
    elif salario > 1200 and salario <= 2000:
        desconto = salario*0.25
        salarioliq = salario - desconto
        print(f'O salário bruto é R$:{salario:.2f} o desconto é de R$:{desconto:.2f} e o salário líquido é R$:{salarioliq:.2f} ')
    else:
        desconto = salario*0.3
        salarioliq = salario - desconto
        print(f'O salário bruto é R$:{salario:.2f} o desconto é de R$:{desconto:.2f} e o salário líquido é R$:{salarioliq:.2f} 'f'')
#ex9
def ex9():
    salario = float(input('Insira seu salário: '))
    salario_anual = salario*13
    if salario_anual <= 15764.28:
        print('Não é contribuinte.')
    elif salario_anual > 15764.28 and salario_anual <= 31501.44:
        aliquota = salario_anual*0.15
        print(f'A contribuição anual deve ser de {aliquota:.2f}')
    else:
        aliquota = salario_anual*0.275
        print(f'A contribuição anual deve ser de {aliquota:.2f}')
#ex10
def ex10():
    peso = float(input('Insira seu peso(Kg): '))
    altura = float(input('Insira sua altura(m): '))
    imc =  peso / (altura  * 2)
    if imc < 18.5:
        print(f'Você está abaixo do peso ideal e seu IMC é {imc}')
    elif imc >=18.5 and imc <= 24.9:
        print(f'Parabéns — você está em seu peso normal! e seu IMC é {imc}')
    elif imc >24.9 and imc <= 29.9:
        print(f'Você está acima de seu peso (sobrepeso) e seu IMC é {imc}')
    elif imc > 29.9 and imc <=34.9:
        print(f'Obesidade grau I e seu IMC é {imc}')
    elif imc >34.9 and imc <= 39.9:
        print(f'Obesidade grau II e seu IMC é {imc}')
    else:
        print(f'Obesidade grau III e seu IMC é {imc}')
#ex11
def ex11():
    sexo = str(input('''Insira o seu sexo [M] ou [F]: ''')).upper()
    salario = float(input('Insira seu salário: '))
    tempo = int(input('Insira os anos completos que possui trabalhados na empresa: '))
    dependentes = int(input('Insira o números de dependentes do funcionário: '))
    while sexo not in ('M', 'F'):
        sexo = str(input('''Insira o seu sexo [M] ou [F]: ''')).upper()
    while salario < 0:
        salario = float(input('Salário inválido, insira novamente seu salário: '))
    while tempo < 0:
        tempo = int(input('Tempo inválido, insira novamente os anos trabalhados: '))
    while dependentes < 0:
        dependentes = int(input('Número inválido,insira novamente o números de dependentes do funcionário: '))

    if dependentes == 0:
        if sexo == 'M':
            if tempo >= 10:
                novosalario = salario * 1.05
                reajuste = novosalario - salario
                print(f'O seu salário atual é {salario:.2f} o reajuste é de {reajuste} e o seu novo salario é {novosalario}')
            else:
                novosalario = salario * 1.03
                reajuste = novosalario - salario
                print(f'O seu salário atual é {salario:.2f} o reajuste é de {reajuste} e o seu novo salario é {novosalario}')
        else:
            if tempo >= 8:
                novosalario = salario * 1.05
                reajuste = novosalario - salario
                print(f'O seu salário atual é {salario:.2f} o reajuste é de {reajuste} e o seu novo salario é {novosalario}')
            else:
                novosalario = salario * 1.03
                reajuste = novosalario - salario
                print(f'O seu salário atual é {salario:.2f} o reajuste é de {reajuste} e o seu novo salario é {novosalario}')
    else:
        if sexo == 'M':
            if tempo >= 10:
                novosalario = (salario * 1.05)*1.02
                reajuste = novosalario - salario
                print(f'O seu salário atual é {salario:.2f} o reajuste é de {reajuste} e o seu novo salario é {novosalario}')
            else:
                novosalario = (salario * 1.03)*1.02
                reajuste = novosalario - salario
                print(f'O seu salário atual é {salario:.2f} o reajuste é de {reajuste} e o seu novo salario é {novosalario}')
        else:
            if tempo >= 8:
                novosalario = (salario * 1.05)*1.02
                reajuste = novosalario - salario
                print(f'O seu salário atual é {salario:.2f} o reajuste é de {reajuste} e o seu novo salario é {novosalario}')
            else:
                novosalario = (salario * 1.03)*1.02
                reajuste = novosalario - salario
                print(f'O seu salário atual é {salario:.2f} o reajuste é de {reajuste} e o seu novo salario é {novosalario}')
#menu da list
while True:
    exercicioaserrodado = int(input('Digite o exercício que deseja rodar: '))
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
        10: ex10,
        11: ex11
    }
    if exercicioaserrodado in biblioteca:
        biblioteca[exercicioaserrodado]()
    else: print('exercício não encontrado! ')
