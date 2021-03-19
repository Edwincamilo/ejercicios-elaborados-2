# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 19:02:56 2021

@author: 57314
"""

cuadradonumero =0
acomuladorsuma =0
acomuladornumero =0
contadorrepeticioneswhile =1

#inicio
cantidadenumeros=int(input("cantidad de numeros:"))

#proceso
while contadorrepeticioneswhile<=cantidadenumeros:
    cuadradonumero =contadorrepeticioneswhile*contadorrepeticioneswhile
    acomuladorsuma = acomuladorsuma + acomuladornumero
    print("el cuadrado de :",contadorrepeticioneswhile,"es:",cuadradonumero)
    print("la suma acomulada es:",acomuladorsuma)
    contadorrepeticioneswhile=contadorrepeticioneswhile+1
    
    #salida
print("la sumade los cuadrados es :", acomuladorsuma)