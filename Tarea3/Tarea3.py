def mediana_arreglos(A, B, n, k):
    if len(A) == 1 and len(B) == 1:
        print(k)
        print(A[0])
    
    else:
        m1 = A[(n+1)//2]
        m2 = B[(n+1)//2]

        if m1 == m2:
            print(k)
            print(A[(n+1)//2])

        elif m1 < m2:
            temp1 = []
            i = n//2
            while i < n:
                temp1.append(A[i])
                i += 1

            temp2 = []
            i=0
            for i in range(n//2):
                temp2.append(B[i])

            mediana_arreglos(temp1, temp2, n//2, k)

        else:
            temp1 = []
            for i in range(n//2):
                temp1.append(A[i])

            temp2 = []
            i = n//2
            while i < n:
                temp2.append(B[i])
                i += 1

            mediana_arreglos(temp1, temp2, n//2, k)

k = int(input())
retornos = []
for _ in range(k):
    n = int(input())
    linea1 = input()
    linea1 = linea1.split(" ")
    linea2 = input()
    linea2 = linea2.split(" ")

    for i in range(n):
        linea1[i] = int(linea1[i])
        linea2[i] = int(linea2[i])

    mediana_arreglos(linea1, linea2, n, k)