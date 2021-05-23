'''
Timelimit: 1
El doctor te ha dado una dieta, en la que cada carácter corresponde a alguna comida que deberías comer.
 También sabes lo que has comido en el desayuno y almuerzo, y cada carácter corresponde a un tipo de comida 
 que ya has ingerido ese dia. Has decidido comer el resto de los alimentos de la dieta durante la cena, 
 y quieres imprimir eso como una cadena (ordenada alfabéticamente). Si hiciste trampa de alguna manera 
 (ya sea comiendo demasiado de un tipo de comida, o comiendo alguna comida que no está en el plan de dieta),
  deberías imprimir la cadena “CHEATER”(entre comillas para destacar).

Entrada
La entrada contiene varios casos de prueba. La primera línea de entrada contiene un entero N que representa 
el número de casos de prueba. Cada caso de prueba está compuesto por tres cadenas, cada una de ellas en una 
línea separada y representa una comida de la dieta, desayuno y almuerzo, respectivamente. Cada cadena contendrá
 de 0 a 26 caracteres('A'-'Z'), y pueden estar vacías.

Salida
Por cada caso de prueba imprimir una cadena que representa comidas que deberías comer durante la cena, o la 
cadena “CHEATER” si hiciste trampa durante la dieta.
'''


def plan_dieta(comidas):
    '''Diccionario que contiene los tipos de alimentos que debes comer(Letras) {letra:1}'''
    plan=dict.fromkeys(comidas[0],1)
    trampa=False
    '''
        Iteramos las letras para el desayuno y el almuerzo
        para cada caso si la letra se encuentra en el diccionario
        reducimos un entero a su valor.
    '''
    for i in range(1,3):
        for alimento in comidas[i]:
            if alimento in plan:
                plan[alimento]-=1
                ''' Si comiste mas de una vez un tipo de alimento trampa=True'''
                if plan[alimento]<0:
                    trampa=True
                '''Si comiste un alimento que nono esta en en el plan, trampa=True'''
            else:
                trampa=True
    
    if(trampa==True):
        return "CHEATER"
    else:
        cadena=""
        for alimento in sorted(list(plan.keys())):
            if plan[alimento]==1:
                cadena+=alimento
        return cadena





N=int(input())
cadena=""
comidas=[]
for i in range(1,N*3+1):
    cadena=input()
    comidas.append(cadena)
    if(i%3==0):
        result=plan_dieta(comidas)
        print(result)
        comidas.clear()

    


    