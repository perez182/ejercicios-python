def acarreos(num1,num2):
    num_acarreos=0
    acarreo=0
    numero1=list(num1)
    numero2=list(num2)
    i=0
    while(len(numero1)>len(numero2)):
        numero2.insert(i,0)
        i+=1
    j=0
    while(len(numero1)<len(numero2)):
        numero1.insert(j,0)
        j+=1
    

    for k in reversed(range(0,len(numero1))):
        suma=int(numero1[k])+int(numero2[k])+acarreo
        if(suma>9):
            acarreo=1
            num_acarreos+=1
        else:
            acarreo=0

    if num_acarreos==0:
        print('No carry operation.')
    elif num_acarreos==1:
        print('1 carry operation.')
    else:
        print("%d carry operations." % num_acarreos)

    
casos_prueba=""
while (True):
    casos_prueba=input()
    if(casos_prueba.count('0 0')!=0):
        break
    numeros=casos_prueba.split(' ')
    result=acarreos(numeros[0],numeros[1])







