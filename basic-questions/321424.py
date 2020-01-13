

base = int(input("Ingrese un numero entero como base: "))
exponente = int(input("Ingrese otro numero entero como exponente: "))
resultado = base



if base>=0 and exponente==0:

    #una base mayor o igual a cero elevada a cero es 1
    resultado = 1

elif base==0 and exponente<0:

    raise Exception('La base no puede ser 0 si el exponente es menor a cero')

else:

    if (exponente < 0):
        exponente = exponente * -1
        resultado = 1 / base
        base = 1 / base

    for i in range(exponente - 1):

        resultado = resultado * base


print("El resultado es: ", resultado)
