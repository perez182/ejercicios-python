'''En este problema tienes que leer un valor entero y calcular el menor número posible de billetes en que puede ser descompuesto. 
Los billetes posibles son 100, 50, 20, 10, 5, 2 y 1. Imprimir el valor leído y la lista de billetes.

Entrada
La entrada contiene un valor entero N (0 < N < 1000000).

Salida
Imprimir el número leído y la cantidad mínima necesaria de billetes en lenguaje portugués, como muestra el ejemplo.
 No olvides imprimir el final de línea luego de cada línea, de otra forma recibirás “Presentation Error”.'''

import math

def cambio_billetes(N):
    billetes=[100,50,20,10,5,2,1]
    cambio=dict.fromkeys(billetes,0)
    
    while(N!=0):
        division=0
        numero_de_billetes=1000000
        for billete in billetes:
            division=math.floor(N/billete)
            if(division<numero_de_billetes and division!=0):
                numero_de_billetes=division
                N=N%billete
                cambio[billete]=numero_de_billetes
                if(N==0):
                    break
    return cambio


N=int(input())
result=cambio_billetes(N)
print(N)
print('%d nota(s) de R$ 100,00' % result.get(100))
print('%d nota(s) de R$ 50,00' % result.get(50))
print('%d nota(s) de R$ 20,00'% result.get(20))
print('%d nota(s) de R$ 10,00'% result.get(10))
print('%d nota(s) de R$ 5,00'% result.get(5))
print('%d nota(s) de R$ 2,00'% result.get(2))
print('%d nota(s) de R$ 1,00'%result.get(1))





