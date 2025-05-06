def function(num1):
    if num1 % 2 == 0:
        print("Este número es par") 
    else:
        print("Este número es inpar") 
        
        
def mayoria(num):
    if num >= 18:
        print("Es mayor de edad") 
    else:
        print("Es menor de edad")
        
def temp(num):
    return (num - 32) * (5/9)

def area(base,altura):
    return (base*altura)/2

def mayor_lista(num):
    mayor = 0
    for i in num:
        if i > mayor:
            mayor = i
        else:
            continue
    return  f"El número más grande es: {mayor}"

def count_letter(palabra,letra):
    return f"La letra {letra} se repite: {palabra.count(letra)} veces"

def filtrar_pares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            continue
    return f"Los pares son: {pares}"

def palíndromo(palabra):
    lista = list(palabra)
    lista_inversa = lista.copy()
    lista_inversa.reverse()
    if lista == lista_inversa:
        print("Es palíndromo")
    else:
        print("No es palíndromo")