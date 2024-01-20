import clase_opreraciones
lista=[]
nums=int(input("Ingrese la cantidad de numeros a ingresar: "))

for i in range(nums):
    num=int(input("{}:Ingresa el numero: ".format(i+1)))
    lista.append(num)

lista.sort()
clase_opreraciones.main(lista)