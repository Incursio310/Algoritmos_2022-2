from cmath import inf

"""
cambio
------------------------
D_arreglo : list
m : int
n : int
i : int
min : int
min_actual : int
suma : int
------------------------
Función que resuelve el problema solicitado, comenzando por la determinación más grande y buscando las combinaciones mínimas
con el resto de monedas para alcanzar el cambio necesario, llamandose a si misma recursivamente para iterar en el arreglo de determinaciones.
Imprime la cantidad mínima de monedas a dar para la cantidad cambio solicitada.

"""

def cambio(D_arreglo, m, n, i, min, min_actual, suma):
    if(i == m):
        print("Cantidad minima de monedas a dar para la cantidad de dinero indicada: ", min)
        return
    else:
        for j in range(i, m):          
            while(suma+D_arreglo[j] <= n):
                suma += D_arreglo[j]
                min_actual += 1

        if(min_actual < min):
            min = min_actual
            
        i+=1
        cambio(D_arreglo, m, n, i, min, 0, 0)

n = int(input())
m = int(input())

D = []

for a in range(0, int(m)):
    aux = input()
    D.append(int(aux))

D.sort(reverse = True)
cambio(D, m, n, 0, inf, 0, 0)
        
