c = 1

while c <= 3:

    numero = int(input('digite o {}° numero: '.format(c)))

    if numero > maior:

        maior = numero

    if numero < menor:

        menor = numero
        
    c = c + 1
    
print('o maior numero digitado foi {}'.format(maior))
print('o menor numero digitado foi {}'.format(menor))