# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:23:29 2022

@author: jazwi
"""
"""
1
"""
def Nazwa(name: str, surname: str):
    return(f'czesc, {name} {surname}!')

czlowiek = Nazwa('jan','kowalski')

print(czlowiek)

"""
2
"""
def Mnozenie(a: int, b: int):
    return(a*b)

liczba = Mnozenie(5,2)

print(liczba)
"""
3
"""
def Parzysta(a: int):
    if a%2 == 0:
        return True
    else:
        return False
    
liczba1 = Parzysta(10)

if liczba1 == True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
"""
4
"""   
def Liczby(a: int, b: int, c: int):
    if a+b >= c: 
        return True
    else:
        return False
    
print(Liczby(3,4,10))
"""
5
"""
def Sprawdzanie(a: list, b: int):
    if b in a:
        return True
    else:
        return False
    
print(Sprawdzanie([1,2,3,4], 2))
"""
6
"""
def Listy(lista1: list, lista2: list):
    final_list = lista1 + lista2
    final_list = list(dict.fromkeys(final_list))
    return [x**3 for x in final_list]

print(Listy([1,2,3,4],[2,3,6,10]))
    






