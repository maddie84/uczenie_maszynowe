# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:46:01 2022

@author: jazwi
"""
"""
a
"""

imiona = ['Ania', 'Kasia', 'Magda']
imiona2 = ['Artur', 'Kacper', 'Piotr']

def WyswietlenieImion(lista = []):
    
    for x in lista:
        print(x)
    
WyswietlenieImion(imiona2)

"""
b
"""

def Liczby(lista1 = []):
    
    return[x*2 for x in lista1]
 
print(Liczby([2,3,4]))
        

def Liczby1(lista1 = []):
    
    lista2 =[]
    
    for x in lista1:
        lista2.append(x*2)
    return lista2
    
print(Liczby([2,3,4]))

"""
c
"""

def Numbers(lista = []):
    return[x for x in lista if x%2==0]

liczby = [*range(1,10)]

print(Numbers(liczby))

"""
d
"""

def Numbers(lista = []):
    print(lista[::2])

liczby = [*range(1,10)]

print(Numbers(liczby))




