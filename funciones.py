def saludo(nombre):
    print(f"Hola {nombre}, cómo estás?")

def suma(num1,num2):
    return num1+num2

def par(num1):
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
        
def factorial(num):
    fact = 1
    i = 1
    while i <= num:
        fact *= i
        i += 1
    return fact

def noDuplicados(list):
    newList=[]
    for item in list:
        if item not in newList:
            newList.append(item)
    return newList

def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 == 0): 
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif (num % 5 == 0): 
        print("Buzz")

def vocales(palabra):
    count=0
    vocales = "aeiouAEIOU"
    for letra in palabra:
        if letra in vocales:
            count += 1
    return count

def invertir(palabra):
    x=list(palabra)
    x.reverse()
    y=",".join(x)
    y=y.replace(",","")
    return y

import re

def validar_contraseña(contraseña):
    if not re.search("[A-Z]", contraseña):
        return False

    if not re.search("[a-z]", contraseña):
        return False

    if not re.search("[0-9]", contraseña):
        return False

    if not re.search("[^a-zA-Z0-9]", contraseña):
        return False

    return True

import random

def lanzar_dado():
    return random.randint(1, 6)

def sumaUnicos(list):
    newList=[]
    for item in list:
        if item not in newList:
            newList.append(item)
    suma=sum(newList)
    return suma

import random
import string

def randompassword(length):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string
