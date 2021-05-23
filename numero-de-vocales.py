'''Vocales en una cadena de texto'''

def num_vocales(cadena):
    vocales_in_cadena=[]
    dicc_vocales=dict.fromkeys(['a','e','i','o','u'],0)

    for letra in cadena:
        if letra in dicc_vocales:
            dicc_vocales[letra]+=1
            vocales_in_cadena.append(letra)
    vocales_in_cadena=sorted(vocales_in_cadena)
    return dicc_vocales,vocales_in_cadena

cadena="esta es mi primera cadena"
dic_vocales,list_vocales=num_vocales(cadena)
print(dic_vocales)
print(list_vocales)