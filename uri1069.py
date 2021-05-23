''' John esta trabajando en una mina de diamante, tratando de extraer la mayor cantidad de diamantes "<>". El debe evitar todas las particulas de arena encontrada "." en este proceso y luego el diamante se puede extraer y nuevos diamantes se pueden formar. Si tiene como entrada. <... << .. >> ....> .... >>>. tres diamantes se han formado. El primero se toma de <..> resultando. <... <> ....> .... >>>. El segundo diamante es entonces retirado, dejando. <.......> .... >>>. El tercer diamante es entonces retirado, dejando al final ..... >>>. con la posibilidad de extraer nuevos diamantes.

Entrada
Leer un entero N que es el número de casos de prueba. Entonces siguen las N líneas, cada una hasta 1000 carateres, incluyendo "<" ,">" y "."

Salida
Debes imprimir la cantidad de diamantes que se han podido extraer en cada caso de prueba. '''



def GetDiamond(cadena):
    pila=[]
    number_diamonds=0
    for caracter in cadena:
        if caracter=='<':
            pila.append(caracter)
        elif caracter=='>':
            try:
                pila.pop()
                number_diamonds+=1
            except:
                pila.append(caracter)
    return number_diamonds



N=int(input())
array_diamonds=[]

for i in range(N):
    cadena=input()
    diamonds=GetDiamond(cadena)
    array_diamonds.append(diamonds)

for total_diamonds in array_diamonds:
    print(total_diamonds)




