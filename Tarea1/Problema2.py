"""
sumas
----------------------
valores : list
valor_actual : int
valor_max = int
i : int
----------------------
Función que resuelve la problemática planteada, realizando backtracking recursivo para seleccionar las combinaciones posibles 
para conseguir la suma del número "t" entregado.
No retorna nada.
"""
def sumas(valores, valor_actual, valor_max, i):
    if(i==len(valores)):
        sum = 0
        for j in range(0, len(sol)):
            if sol[j] == 1:
                sum += valores[j]
        if sum == valor_max:
            crearLista(sol)

            
        return

    if valor_actual + valores[i] <= valor_max:
        sol.append(1)
        sumas(valores, valor_actual+valores[i], valor_max, i+1)
        sol.pop()
    sol.append(0)
    sumas(valores, valor_actual, valor_max, i+1)
    sol.pop()

"""
crearLista
-------------------------
solucion : list
-------------------------
Función que utiliza los valores binarios de la lista solución para construir las distintas respuestas
al problema presentado.
No retorna nada.
"""

def crearLista(solucion):
    string = ""
    for j in range(0, len(solucion)):
        if solucion[j] == 1 and string == "":
            string = string + str(L[j])
        elif(solucion[j] == 1 and string != ""):
            string = string + "+" + str(L[j])

    if string not in lista:
        lista.append(string)

flag = True
while(flag):
    L = []
    sol = []
    lista = []
    a = input()
    a = a.split(" ")
    for k in range(0, len(a)):
        a[k] = int(a[k])

    t = a[0]

    for l in range(2, a[1]+2):
        L.append(a[l])

    if a[1] == 0:
        flag = False

    if flag == True:
        sumas(L, 0, t, 0)
        print("Suma de "+ str(t)+":")
        if len(lista) != 0:
            for m in range(0, len(lista)):
                print(lista[m])
        else:
            print("NADA")



