mayor = 0
residuo  = 0

n1 = int(input("Ingrese un número"))
n2 = int(input("Ingrese un número"))
if n1 > n2:
    mayor = n1
elif n2 > n1:
    mayor = n2
print("El número mayor es: ",mayor)


numeros = 0 
while numeros < mayor:
    numeros = numeros + 1
    print(numeros)
