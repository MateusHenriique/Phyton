NOME = str(input('digite seu nome completo: ')).lower().strip()
NOME = NOME.split()
print('prazer em te conhecer!')
print('seu primeiro nome é {}'.format(NOME[0]))
print('seu ultimo nome é: {}'.format(NOME[len(NOME) - 1])) #podemos ler uma serie de palavtas de tras para frente usando o len para ler e o -1 para identificarmos que quewremos ler começando da ultima palavra (passo -1)