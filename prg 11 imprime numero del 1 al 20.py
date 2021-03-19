# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:03:09 2021

@author: 57314
"""

# programa que lee una tabla y la imprime del 1 hasta el 20 y suma los resultados

#declarar tablas

tabla= 0
multiplicador = 1
resultado = 0
sumaresultado = 0
conRepCiclo = 1 

#leer la tabla para la cual vamos a realizar las operaciones 
tabla = int(input("tabla :"))


# leer el multiplicador

multiplicador = int(input("multiplicador:"))


# inicio del ciclo repetitivo while

while(conRepCiclo <= multiplicador ):
     resultado = tabla * conRepCiclo
     sumaresultado = sumaresultado + resultado 
     print(tabla," * ",conRepCiclo, " = ",resultado)
     #incrementar variable que controla el ciclo
     conRepCicloCiclo = conRepCiclo + 1
print("la suma de los resultados es:",sumaresultado)