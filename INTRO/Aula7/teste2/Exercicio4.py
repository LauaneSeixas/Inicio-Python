#ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS.

n1 = int(input('Digite o valor em metros: '))
cm = n1*100
ml = n1*1000
print('O valor em cetimetros é de: {}, em milimetros é de: {}'.format(cm, ml))
