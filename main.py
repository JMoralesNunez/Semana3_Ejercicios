from funciones import *

num = int(input("Enter a number: "))
par(num)

edad = int(input("Enter your age: "))
mayoria(edad)  


temperatura = int(input("Enter your temp in F°: "))
temperatura=temp(temperatura)
print(temperatura)


base = int(input("Ingresa la base del triangulo: "))
height = int(input("Ingresa la altura del triangulo: "))
triangulo = area(base,height)
print(triangulo)

lista = [2,3,4,18,7,8,2,7,9]
numMayor = mayor_lista(lista)
print(numMayor)

palabra = input("Ingrese una palabra: ")
letra = input("Ingrese la letra que desea contar dentro de la palabra: ")
cuenta = count_letter(palabra,letra)
print(cuenta)

lista = [2,3,4,18,7,8,2,7,9]
lista_pares = filtrar_pares(lista)
print(lista_pares)

palíndroma = input("Ingrese una palabra: ")
palíndromo(palíndroma)

print(factorial(4))

print(noDuplicados([1,2,2,3,4,5,5,6,7,8,8,9]))

fizzbuzz(15)

print(vocales("palabra"))

print(invertir("Queso"))

print(validar_contraseña("Riwi123#"))

print(lanzar_dado())

print(sumaUnicos([1,2,2,3,4,5,5,6,7,8,8,9]))

print(randompassword(10))
