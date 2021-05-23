
def arbol_pascal(num_filas):
    arbol_pascal=[]
    for i in range(num_filas):
        fila=[]
        for j in range(i+1):
            if(j==0 or j==i):
                fila.append(1)
            else:
                valor=arbol_pascal[i-1][j-1]+arbol_pascal[i-1][j]
                fila.append(valor)
        arbol_pascal.append(fila)
    return arbol_pascal

arbol=arbol_pascal(7)

for fila in arbol:
    print(fila)


    
    

    

    
    