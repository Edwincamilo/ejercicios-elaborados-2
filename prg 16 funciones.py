# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 18:59:05 2021

@author: 57314
"""

#factura a pagar 

def f_titulo():
    print("calculo valor factura")
    
    
def f_despedida():
    print("gracias por su compra")
    

def f_valorfactura(): #encabezado de la funcion 
    #desarollo de la funcion 
    #definion de variablas
    
    ve_nomArt =""
    ve_canArt =0
    ve_valUnitArt=0.0
    
    cons_porceniva=0.19
    
    vaprosali_netopag=0.0
    vaprosali_ivapag=0.0
    vaprosali_totalpag=0.0
    
    #entradas 
    ve_nomArt =input("Articulo:")
    ve_canArt =int(input("cantidad:"))
    ve_valUnitArt = float(input("valor unitario:"))
    
    #procesos 
    
    vaprosali_netopag= ve_canArt * ve_valUnitArt
    vaprosali_ivapag = vaprosali_netopag * cons_porceniva
    vaprosali_totalpag = vaprosali_netopag+ vaprosali_ivapag
    
    
    #salidas 
    print("neto:",vaprosali_netopag)
    print("iva:",vaprosali_ivapag)
    print("total:",vaprosali_totalpag)
    
    
 # llamado a la funcion
f_titulo()
f_valorfactura()
f_despedida()
