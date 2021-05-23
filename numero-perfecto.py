# En matemáticas, un número perfecto es un número entero para el cual la suma de todos 
# sus propios divisores positivos (excluyéndose a sí mismo) es igual al número en sí.
# Por ejemplo, el número 6 es perfecto, porque 1 + 2 + 3 es igual a 6. 
# Tu tarea es escribir un programa que lea números enteros e imprima un mensaje 
# informando si estos números son perfectos o no son perfectos.

import sys

def perfect_number(numero):
    suma=0
    for i in range(1,int(numero/2)+1):
        if((numero%i)==0):
            suma+=i
    if(suma==numero):
        return str(numero)+" "+"eh perfeito"
    else:
        return str(numero)+" "+"nao eh perfeito"

entradas=int(input())
for i in range(entradas):
    N=int(input())
    result=perfect_number(N)
    print(result)
    


