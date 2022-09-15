lista = [16,21,22,
18,23,24,
20,25,26,
22,27,28,
24,29,30] #tampinhas

def min():
    i = 0 #iterador
    min = float('inf') #saco vazio 
    while (i < len(lista)): 
        if (min >= lista[i]):   
            min = lista[i]  
        i += 1 #andando com o carrinho    
    print(min)
       
def max():
    i = 0
    max = 0
    while (i < len(lista)):
        if (max <= lista[i]):
            max = lista[i]
        i += 1
    print(max)

def soma():
    i = 0 #iterador
    soma = 0 #saco vazio 
    while (i < len(lista)):
        soma += lista[i]      
        i += 1 #andando com o carrinho    
    print(soma)

def inver():
    i = 0
    inver = 0
    while (i < len(lista)):
        inver = -lista[i]
        print(inver)
        print('.........')
        i += 1


def rodar_operacao():

    op = input("Escolha uma operação: ")
    
    if (op == 'min'):
        min()
    elif (op == 'max'):
        max()
    elif (op == 'soma'):
        soma()
    elif (op == 'cancelar'):
        return False
    elif (op == 'inverter'):
        inver()
    else:
        print('operação inválida')
    return True

print("Tampinhas disponíveis")
print(lista)
print("operações disponiveis:")
print("min, max, soma, inverter, ou, cancelar", end=" ")
print(" ")

conti = True

while(conti):
    conti = rodar_operacao()

print('obrigado pela partipação')

