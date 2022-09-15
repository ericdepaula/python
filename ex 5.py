number = [12, 75, 150, 180, 145, 525, 50]

for i in number:
    
    if i > 500: # Se maior que 500
        break #para o loop
    elif i > 150: #se maior que 150 
        continue #continua o Loop
    elif i % 5 == 0: #Verifica se o numero é divisivel por 5
        print(i)