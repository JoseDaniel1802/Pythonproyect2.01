mayor = 0
residuo  = 0
n1 = int(input("Ingrese un número"))
n2 = int(input("Ingrese un número"))
if n1 > n2:
    mayor = n1
elif n2 > n1:
    mayor = n2
print("El número mayor es: ",mayor)
residuo = mayor // 2
if residuo == 0:
    print(f'El número {mayor} es par por que su residuo es 0')
elif residuo != 0:
    print(f'El número {mayor} es impar por que su residuo es {residuo}')
numeros = 0 
while numeros < mayor:
    numeros = numeros + 1
    print(numeros)

