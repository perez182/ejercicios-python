billetes=[100,50,20,10,5,2]
monedas=[100,50,25,10,5,1]


N=float(input())

print('NOTAS:')
for billete in billetes:
    division=int(N/billete)
    modulo=(N%billete)   
    N=modulo
    print('%d nota(s) de R$ %.2f'% (division,billete))

N=N*100
N=round(N)

'''Desconozco por que '''
#print('MOEDAS:')
#for moneda in monedas:
#    division=int(N/moneda)
#    modulo=N%moneda
#    N=modulo
#    moneda_imprimir=float(moneda/100)
#    print('%d moeda(s) de R$ %.2f'% (division,moneda_imprimir))
        
'''Por lo tanto tuve que imprimirlo asi'''

print('MOEDAS:')
division=int(N/100)
modulo=N%100
N=modulo
print('%d moeda(s) de R$ 1.00'% division)

division=int(N/50)
modulo=N%50
N=modulo
print('%d moeda(s) de R$ 0.50'% division)

division=int(N/25)
modulo=N%25
N=modulo
print('%d moeda(s) de R$ 0.25'% division)

division=int(N/10)
modulo=N%10
N=modulo
print('%d moeda(s) de R$ 0.10'% division)

division=int(N/5)
modulo=N%5
N=modulo
print('%d moeda(s) de R$ 0.05'% division)

division=int(N/1)
modulo=N%1
N=modulo
print('%d moeda(s) de R$ 0.01'% division)



