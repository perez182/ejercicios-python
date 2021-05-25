'''
Guga tiene una cadena S que contiene sólo letras minúsculas y quiere hacer algunas operaciones en ella. Cada operación puede ser uno de los siguientes tipos:

0 x, mueva cada vocal de S x posiciones de izquierda a derecha. (Comenzando de nuevo al principio si es necesario).

1 x, mueva cada consonante en S x posiciones de izquierda a derecha. (Comenzando de nuevo al principio si es necesario)

2, imprima S tal como está.

Las vocales que estamos considerando son las letras a, e, i, o y u.
Una operación de tipo 0 sólo mueve las vocales a través de posiciones en S que contienen vocales.
Una operación de tipo 1 sólo mueve consonantes a través de posiciones en S que contienen consonantes.


Por ejemplo,

La cadena "computador" después de la operación 1 2 se convierte en "dorcumapot", es decir,
 cada consonante va a la posición de la segunda consonante siguiente.

La cadena "abe" después de la operación 0 1 se convierte en "eba".

Entrada
La primera línea de entrada contiene un entero T (1 ≤ T ≤ 100), que es el número de casos de prueba.
La primera línea de cada caso de prueba contiene S (1 ≤ |S| ≤ 10⁴), que es la cadena de Guga.
La segunda línea de entrada contiene un entero Q (1 ≤ Q ≤ 10⁵),
que es el número de operaciones que Guga va a hacer en S. 
Cada una de las siguientes Q líneas contiene operaciones como las descritas anteriormente.
Para cada operación, 0 ≤ x ≤ |S|.

Salida
Para cada caso de prueba, imprima “Caso #X:”, donde X es el número del caso actual,
comenzando en 1. Para cada operación del tipo 2, 
imprima en una nueva línea con la cadena S después de haber aplicado todas las operaciones anteriores sobre ella.
El archivo de salida contiene alrededor de 3*10⁶ caracteres.
'''

def operacion_0(cadena,num_saltos):
    num_saltos=int(num_saltos)
    array_cadena_final=list(cadena)
    vocales=dict.fromkeys(['a','e','i','o','u'])
    posiciones=[]

    for i in range(len(cadena)):
        if cadena[i] in vocales:
            posiciones.append(i)

    for i in range(len(posiciones)):
        new_posicion=(i+num_saltos)%len(posiciones)
        array_cadena_final[posiciones[new_posicion]]=cadena[posiciones[i]]
    return "".join(array_cadena_final)

def operacion_1(cadena,num_saltos):
    num_saltos=int(num_saltos)
    array_cadena_final=list(cadena)
    vocales=dict.fromkeys(['a','e','i','o','u'])
    posiciones=[]

    for i in range(len(cadena)):
        if (cadena[i] in vocales)==False:
            posiciones.append(i)
    

    for i in range(len(posiciones)):
        new_posicion=(i+num_saltos)%len(posiciones)
        array_cadena_final[posiciones[new_posicion]]=cadena[posiciones[i]]
    return "".join(array_cadena_final)


T=int(input())

for i in range(T):
    S=input()
    Q=int(input())
    print("Caso #"+str(i+1)+":")
    for j in range(Q):
        operacion=str(input())
        operaciones=operacion.split(' ')
        if operaciones[0]=='0':
            S=operacion_0(S,operaciones[1])
        elif operaciones[0]=='1':
            S=operacion_1(S,operaciones[1])
        else:
            print(S)






