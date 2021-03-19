# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 18:36:15 2021
leer N  y calcular esa cantidad de numeros aleatorios y promediarlos
@author: 57314
"""

suma =0 
primedio = 0 
contadorrepeticiones = 0 
promedionumerosaleatorios = 0.0
numero =0
#variables segunda parte del ejercicio
acomuladorpositivos=0
acomuladordenegativos=0
promediodepositivos =0.0
promediodenegativos=0.0
contadorpositivos =0
contadornegativos=0
#variables tercera parte del ejercicio
mayorpositivo=0
mayornegativo=0
menorpositivo=100
menornegativo=0


# libreria usada 
import random

#entrada

cantidadnumeros= int(input("digite cantidad de numeros :"))

#procesos 
#ciclo while |
while contadorrepeticiones<cantidadnumeros:
    numero=random.randint(-100,100)
    suma= suma+numero
    #segunda parte del ejercicio
    if numero>0: #calculo numeros positivos 
         print("numero positivo:",numero)
         acomuladorpositivos=acomuladorpositivos+numero
         contadorpositivos=contadorpositivos+1
         #identificar mayor de los positivos
         if numero>mayorpositivo:
             mayorpositivo=numero
        #identificar menor positivo
         if numero<menorpositivo:
            menorpositivo=numero
    else: #calculo para numeros negativos 
        print("numero negativo:",numero)
        acomuladordenegativos=acomuladordenegativos+numero
        contadornegativos=contadornegativos+1
        # identificar el mayor de los negativos
        if numero<mayornegativo:
            mayornegativo=numero
            
        #identificar el menor de los negativos
        if numero>menornegativo:
            menornegativo=numero
            
            
        #fin segfunda parte del ejercicio
    contadorrepeticiones=contadorrepeticiones+1
#fin ciclo
#calculo de los promedios 
promedionumerosaleatorios=suma/contadorrepeticiones
promediodepositivos=acomuladorpositivos/contadorpositivos
promediodenegativos=acomuladordenegativos/contadornegativos

#salida para todos los numeros
print("suma de numeros aleatorios :",suma)
print("promedio de numeros aleatorios ;",promedionumerosaleatorios)


#salida para numeros positivos

print("cantidad numeros positivos:",contadorpositivos)
print("suma de numeros positivos:",acomuladorpositivos)
print("promedio de numeros positivos:",promediodepositivos)

#salida para numero negativos
print("cantidad de numeros negativos:",contadornegativos)
print("suma de numeros negativos:",acomuladordenegativos) 
print("promedio de numeros negativos:",promediodenegativos)  

#imprimir mayor y menor de los positivos 
print("mayor de los positivos:",mayorpositivo)
print("menor de los positivos:",menorpositivo)

#imprimir mayor y menor de los negativos 
print("mayor de los negativos:",mayornegativo)
print("menor de los negativos:",menornegativo)

   
    
    
    