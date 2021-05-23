'''Escriba un programa que lea el nombre de un vendedor, su salario fijo y el total de las ventas realizadas por él en el mes (en dinero). Considerando que el vendedor recibe un 15% de los productos vendidos, escribir el salario final (total) de cada vendedor a fin de mes, con dos cifras decimales.

- No olvide de imprimir un final de linea luego del resultado, de otra forma recibirá “Presentation Error”.

- No olvide los espacios en blanco.

Entrada
La entrada contiene un texto (primer nombre del empleado), y dos valores de doble precisión, los cuales representan el salario del vendedor y el valor total vendido por él.

Salida
Imprimir el salario total del vendedor, de acuerdo a los ejemplos. '''

nombre=str(input())
salario=float(input())
ventas=float(input())
total=salario+(ventas*.15)
print('TOTAL = R$ %.2f' % total)
