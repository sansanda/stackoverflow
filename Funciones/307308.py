A=0
B=0
C=0

print(A,B,C)

def numeros(A,B,C):

    A = int(input("ingrese numero uno"))
    B = int(input(" ingrese numero dos"))
    C = int(input("ingrese numero tres"))

    return A, B, C

numeros(A,B,C)

print(A,B,C)

def numero_mayor(A, B, C):
    if (A > B and A > C):
        print("El numero mayor es ", A)
    elif (B > A and B > C):
        print("El numero mayor es ", B)
    else:
        print("El numero mayor es ", C)


a,b,c = numeros()

numero_mayor(a,b,c)