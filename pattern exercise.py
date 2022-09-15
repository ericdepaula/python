print('Pattern exercise')
# quantidade de Linha(rows) que terá
rows = 5

# I analogicamente seria a sacola, enquanto rows o carrinho
for i in range (1, rows + 1):
    # J é o contador de procutos que há na sacola(separadamente)
    for J in range (1, i + 1):
        print(J, end=" ")
    print(' ')
    