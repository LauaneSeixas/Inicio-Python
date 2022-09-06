#FAÇA UM PROGEAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECERRÁRIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M2

n1 = float(input('Digite a altura da parede: '))
n2 = float(input('Digite a largura da parede: '))
a = n1*n2
t = a/2
print('Sua parede tem a dimensão de {} e você vai precisar de {}l de tinta'.format(a, t))