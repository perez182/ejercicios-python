'''Combinar Cadenas'''

'''Implementar un programa Combiner que tome dos cadenas como parámetros y las combine, 
alternando letras, comenzando con la primera letra de la primera cadena, 
seguida de la primera letra de la segunda cadena, luego la segunda letra de la primera cadena,
 etc. los String más largos se añaden al final de la combinación String y se devuelve esta combinación String.'''

'''
input:
La entrada contiene varios casos de prueba. La primera línea de entrada contiene un número entero N
que indica el número de casos de prueba. Cada caso de prueba se compone de una línea que contiene 
dos cadenas y cada cadena contiene entre 1 y 50 caracteres, inclusive.

output:
Combine las dos cadenas de entrada, como se muestra en el siguiente ejemplo, e imprima la cadena resultante.
'''

# Sample Input                       Sample output
# 2                                     TopCoder
# Tpo oCder                               abab
# aa bb


def combiner(cadena):
    palabras=cadena.split(" ")
    cadena1=palabras[0]
    cadena2=palabras[1]
    tamaños=[len(cadena1),len(cadena2)]
    tamaños=sorted(tamaños,reverse=True)
    new_cadena=""
    tamaño=tamaños[0]
    for i in range(tamaño):
        if(i>=len(cadena1)):
            new_cadena+=cadena2[i]
        elif(i>=len(cadena2)):
            new_cadena+=cadena1[i]
        else:
            new_cadena+=cadena1[i]
            new_cadena+=cadena2[i]
    return new_cadena

N=int(input())

for i in range(N):
    cadena=str(input())
    combiner_string=combiner(cadena)
    print(combiner_string)
    
def abreviatura(cadena):
    palabras=cadena.split(" ")
    print(palabras)
    
cadena="hoje eu visitei meus pais"


result=abreviatura(cadena)