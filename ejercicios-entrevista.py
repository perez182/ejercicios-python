"""Calcula el elemento de la posicion  (n) de la serie de Fibonnaci"""

def fibonnacci(n):
    if n==0:
        return 0
    elif (n==1 or n==2):
        return 1
    else:
        return fibonnacci(n-1)+fibonnacci(n-2)


"""Regresa la lista de los primeros n elementos de la serie de fibonnaci"""
def add_fibonacci(n):
    lista=[]
    for e in range(n):
        x=fibonnacci(e)
        lista.append(x)
    return lista


"""Regresa la suma de los elementos en las pocisiones pares de la susecion de 
Fibonnaci en un intervalo de 0 a i, i<=n"""
def suma_fibbonaci(n,i):
    suma=0
    result_list=add_fibonacci(n)
    for x in range(i):
        if ((x%2)==0):
            suma=suma+result_list[x]
    return suma


result_fibonnaci_suma=suma_fibbonaci(10,5)

print(result_fibonnaci_suma)
        


    


        
