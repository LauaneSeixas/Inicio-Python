#FAÇA UM ALGORITMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE SEU NOVO PREÇO, COM 5% DE DESCONTRO

n1 = float(input('Digite o valor do produto: '))
d = n1 - n1 * 0.05
print('Valor com desconto: {}'.format(d))