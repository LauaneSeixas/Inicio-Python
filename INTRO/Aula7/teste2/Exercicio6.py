#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO UMA PESSOA TEM NA CARTEIRA E MOSTRE QUANTOS DÓLARES ELA PODE COMPRAR.
#CONSIDERE: U$1.00 = r$3.27

n1 = float(input('Quanto você tem em reais?'))
d = n1/3.27
print('Você tem {:.2f} doláres'.format(d))
