# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 18:54:54 2021

@author: 57314
"""

#determinar la media de una lista definida de nuemros positivos terminando con un numero negativo

# declaracion de variables 
 
numero = 0     #variable que almacena los numeros que dijite el usuario
suma = 0        #variable que almacena la suma que dijite el usuario
media= 0.0         #variable que almacena la media que dijite el usuario
cantidadelemetos = 0 #variable que almacena la cantidad de elemntos  que dijite el usuario


numero = int(input("numero:")) # lectura del primer nuemro

while (numero > 0):
    suma = suma + numero 
    numero = int (input("numero:")) # lectruras de los otros numeros
    cantidadelemetos = cantidadelemetos +1 
    
# termina el ciclo
if cantidadelemetos !=0:
    media = suma / cantidadelemetos # calcular la media 
    print("la media es:", media) #imprimir la media
    
else:
    print("no hay numero para calcular la media")