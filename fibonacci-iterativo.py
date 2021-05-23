def fibbonacci(n):
    serie_fibonacci=[]
    for i in range(n):
        if(i==0 or i==1):
            serie_fibonacci.append(1)
        else:
            serie_fibonacci.append(serie_fibonacci[i-1]+ serie_fibonacci[i-2])
    return serie_fibonacci


sucesion_fibonacci=fibbonacci(10)
print(sucesion_fibonacci)
        
    