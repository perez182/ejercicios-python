
def abreviatura(cadena):
    '''palabras: arreglo de palabras
       dicc_palabras: diccionario de palabras (palabra,numero_caracteres_totales)
       abreviaturas: diccionario de palabras (palabra,abreviatura)
       agregamos un espacio al final de la cadena'''
    palabras=cadena.split(" ")
    dicc_palabras=dict.fromkeys(palabras)
    abreviaturas=dict.fromkeys(palabras)
    cadena=cadena.replace('.','')+' '

    '''num_caracteres: numero de caracteres que se ahorran
        abreviaturas: se abrevian todas las palabras con su letra inicial+"." con excepcion 
        de las que miden 2 caracteres'''
    for palabra in dicc_palabras:
        num_caracteres=cadena.count(palabra+' ')*len(palabra)-2*cadena.count(palabra+' ')
        dicc_palabras[palabra]=num_caracteres
        if len(palabra)>2:
            abreviaturas[palabra]=palabra[0]+'.'
        else:
            del abreviaturas[palabra]

    "diccionario (abreviaciones,palabras)"
    letras=dict.fromkeys(list(abreviaturas.values()),0)
    
    for palabra in abreviaturas:
        letra=abreviaturas[palabra]
        if letras[letra]==0:
            letras[letra]=palabra
        else:
            if dicc_palabras[palabra]>dicc_palabras[letras[letra]]:
                letras[letra]=palabra
    
    
    for palabra in abreviaturas:
        if letras[abreviaturas[palabra]]!=palabra:
            abreviaturas[palabra]=palabra

    new_texto=""
    for palabra in palabras:
        if(abreviaturas.get(palabra)!=None):
            new_texto+=abreviaturas[palabra]+' '
        else:
            new_texto+=palabra+' '

    print(new_texto[0:len(new_texto)-1])
    print(len(letras))

    for letra in sorted(list(letras)):
        print(letra + ' = ' + letras[letra])
    
    
casos_de_prueba=[]
cadena=""
while(cadena.count('.')==0):
    cadena=str(input())
    casos_de_prueba.append(cadena)
casos_de_prueba.pop()


for caso in casos_de_prueba:
    result=abreviatura(caso)