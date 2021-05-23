'''Leer 100 números enteros. Imprimir el valor leído más alto y la posición de entrada.

Entrada
El archivo de entrada contiene 100 números enteros positivos distintos.

Salida
Imprimir el número más alto leído y la posición de entrada de ese valor, según el ejemplo dado. '''

mayor=0
posicion=0
for i in range(1,101):
    numero=int(input())
    if(numero>mayor):
        mayor=numero
        posicion=i
    
print(mayor)
print(posicion)