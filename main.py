from funciones import function, mayoria, temp, area, mayor_lista, count_letter, filtrar_pares, palíndromo

num = int(input("Enter a number: "))
function(num)

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