def puentes(S1, S2, n):

    matriz = []
    for i in range(n+1): #Se construye la matriz
        matriz.append([0]*(n+1))

    for i in range(n+1):
        for j in range(n+1): #Llena la matriz de izquierda a derecha.
            if i == 0 or j == 0: #Casos bases (fila 0 y columna 0 con 0's)
                matriz[i][j] = 0
            elif S1[i-1] == S2[j-1]: 
                matriz[i][j] = matriz[i-1][j-1] + 1
            else: #Busca el máximo entre la fila anterior y el de la columna anterior y lo coloca en los posición actual.
                matriz[i][j] = max(matriz[i-1][j], matriz[i][j-1])

    index = matriz[n][n] #En  la posición n,n está la solución.

    puentes = [""] * (index+1)

    i = j = n
    while i > 0 and j > 0: #Lo que hace es ver qué caminos son los que se construyen.

        if S1[i-1] == S2[j-1]:
            puentes[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1

        elif matriz[i-1][j] > matriz[i][j-1]:
            i -= 1
        else:
            j -= 1

    print(len(puentes)-1)#Para mantener el formato de salida.
    for k in range(len(puentes)-1):
        print(puentes[k])#Para mantener el formato de salida.

n = int(input())
S1 = []
S2 = []
#Creamos unas listas con las entradas de los puentes, por lo que revisamos las conexiones con este.
for i in range(n):
    S1.append(input())

for i in range(n):
    S2.append(input())

puentes(S1, S2, n)