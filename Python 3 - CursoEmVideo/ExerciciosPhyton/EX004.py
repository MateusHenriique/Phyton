a1 = input('Digite algo: ')
print('O tipo primitivo do que foi digitado é: {}'.format(type(a1)))
print('É alfabetico: {}'.format(a1.isalpha()))
print('É alfanumerico: {}'.format(a1.isalnum()))
print('É numerico: {}'.format(a1.isnumeric()))
print('Está escrito só com maiusculo: {}'.format(a1.isupper()))
print('Está escrito só com minusculos: {}'.format(a1.islower()))
print('Está escrito só com espaços: {}'.format(a1.isspace()))
print('Está captalizada: {}'.format(a1.istitle()))
