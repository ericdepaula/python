    
a = int(input('digite um numero: '))
b = int(input('digite outro numero: '))

num = [a, b]

def soma():
    soma = sum(num)
    print(soma)

def subtracao():
        subtracao = a - b
        print(subtracao)

def multiplicacao():
    multiplicacao = a * b
    print(multiplicacao)

def divisao():
    divisao = a / b
    print(divisao)

def tabuada():
    rows = 10
    for i in range (1, rows + 1):
        p = a * i
        p2 = b * i
        print(p, end=" | ")
        print(p2)

def rodar_operacao():

    op = input("Escolha uma operação: ")
    
    if (op == 'soma'):
        soma()
    elif (op == 'subtrair'):
        subtracao()
    elif (op == 'multiplicar'):
        multiplicacao()
    elif (op == 'divisao'):
        divisao()
    elif (op == 'tabuada'):
        tabuada()
    elif (op == 'cancelar'):
        return False
    else:
        print('operação inválida')
    return True

print('Operações disponíveis: ')
print('soma, subtrair, multiplicar, divisao, tabuada e cancelar')

conti = True

while(conti):
    conti = rodar_operacao()

print('Obrigado por usar meus serviços')