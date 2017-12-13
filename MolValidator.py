# -*- coding: utf-8 -*-

from Elements import elements

# Métodos que se encargan de la validación semantica de las moléculas ingresadas

# Valida que se cumpla el octeto alrededor del elemento central de cada molécula.
# Para esto recupera el número de electrones de valencia del átomo central y lo
# suma a la cantidad de enlaces que se forman sobre él (sumando número de átomos del
# elemento acompañante y el número de enlaces con guión). Si la suma es igual a algún
# número de estabilidad correspondiente al elemento central, entonces se acepta la molécula.

def validateOctect( el, sum ):
    vNum = elements[el]["Valence"]
    st   = elements[el]["Stability"]
    oct = False
    for i in st:
        vNum = vNum + sum
        if(vNum == i):
            oct = True
        vNum = elements[el]["Valence"]
    return oct

# Hace la misma validación pero para el elemento acompañante. Esta hace que solo se acepten
# elementos con una valencia de 7, ya que solo requieren del elemento central para alcanzar el octeto.
# Por cuestiones de tiempo no se hizo más flexible en este aspecto.

def validateBondOctect( bond):
    vNum = elements[bond]["Valence"]
    st   = elements[bond]["Stability"]
    oct = False
    for i in st:
        vNum = vNum + 1
        if(vNum == i):
            oct = True
    return oct

