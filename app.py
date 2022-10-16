import math
print('ATENÇAO')
print('-='*30)
print(''' Orientaçao a baixo pós digitar os numero ''')
print('-='*30)
n=int(input('Digite um numero: '))
n2=int(input('Digite outro numero: ')) 
op=0
while op!=6:
    print('''
    [1]= Mutilplicação)
    [2]= Subtração
    [3]= Adição
    [4]= Divisão
    [5]== Para continuar
    [6] = Sair do programa''')
    op=input('Digite a opçao: ').upper().strip()
    print('-='*30)
    if op == '1':
        print(f'{n} X {n2} = {n*n2}')
    elif op=='2':
        print(f'{n}-{n2}={n-n2}')
    elif op=='3':
        print(f'{n}+{n2}={n+n2}')
    elif op=='4':
        print(f'{n} / {n2}={n/n2} ')
    elif op=='5':
         n=int(input('Digite um numero:'))
         n2=int(input('Digite outro numero: '))
    else:('Operador nao suportado ')
print('Fim do programa')