# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:37:20 2021

@author: 57314
"""

tabla= 0
multiplicador = 1
resultado = 0
sumaresultado = 0
conRepCiclo = 1 

#leer la tabla para la cual vamos a realizar las operaciones 
tabla = int(input("tabla :"))


# leer el multiplicador

multiplicador = int(input("multiplicador:"))

# inicio del ciclo 
for conRepCiclo in range (multiplicador +1):
   
    # inicio del ciclo repetitivo while

    resultado = tabla * conRepCiclo
    sumaresultado = sumaresultado + resultado 
    print(tabla," * ",conRepCiclo, " = ",resultado)
    #incrementar variable que controla el ciclo
  
print("la suma de los resultados es:",sumaresultado)
    