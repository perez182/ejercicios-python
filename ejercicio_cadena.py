
#Problema: Realizar una funcion que calcule el numero de repeticiones de cada palabra en una cadena de texto

''' Se encontraron 2 soluciones '''

def Word_Repetition(texto):
    """Normalizamos el texto"""
    new_cadena=texto.lower().replace(",","").replace(".","")
    """Guardamos la cadena en un array de palabras"""
    array_texto=new_cadena.split(" ")
    dicccionario={}


    """Recorremos una vez el arreglo del texto"""
    for word in array_texto:
        """Buscamos la palabra en el diccionario,
        Diccionario={palaba:numero de repeticiones}
        Si la palabra ya se encuentra registrada en el diccionario su valor incrementa en uno
        Si aun no se encuentra en el diccionario, se agrega la palabra como clave y su valor=1
        """
        if (word in dicccionario):
            dicccionario[word]+=1
        else:
            dicccionario[word]=1
    return dicccionario

def Word_REpetition2(texto):
    """Normalizamos el texto"""
    new_cadena=texto.lower().replace(",","").replace(".","")+' '
    """Guardamos la cadena en un array de palabras"""
    array_text=new_cadena.split(" ")
    diccionario=dict.fromkeys(array_text)

    for palabra in diccionario:
        repeticiones=new_cadena.count(palabra+' ')
        diccionario[palabra]=repeticiones

    return diccionario

cadena="Esta es una Cadena de ejemplo, ejemplo de cadena de texto. Asi es esto es una Cadena"

diccionario=Word_Repetition(cadena)
print()
print(diccionario)

print()
print()
diccionario2=Word_Repetition(cadena)
print()
print(diccionario2)
