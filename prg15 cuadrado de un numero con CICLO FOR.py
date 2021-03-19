# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 15:36:43 2021
cuadrado de numeros 
@author: 57314
"""
cuadradonumero =0
acomuladorsuma =0
num =1
acomuladornumero =0

#inicio
cantidadenumeros=int(input("cantidad de numeros:"))

#proceso

for num in range(1,cantidadenumeros+1,1):#ultimo uno hace referenci al siguiente numero 
    cuadradonumero =num*num
    acomuladorsuma = acomuladorsuma + acomuladornumero
    print("el cuadrado de :",num,"es:",cuadradonumero)
    print("la suma acomulada es:",acomuladorsuma)
    
    #salida
print("la sumade los cuadrados es :", acomuladorsuma)
